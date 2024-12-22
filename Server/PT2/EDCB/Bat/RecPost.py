﻿#
# 説明
#
#  EDCB で録画後に実行するバッチプログラムから呼び出される Python スクリプト。
#  ファイル名、予約キーワード、およびジャンルを引数に取り、録画ファイル（TSファイル）
#  のファイル名に連番をつけたり、副題っぽい名前にしたり、ジャンルや予約キーワードで
#  フォルダ分けしたりする。
#
# 引数
#
# -a | --addkey
# 予約録画時のキーワード (ex. "相棒")
#
# -d | --debug
# デバッグモード
#
# -f | --filepath
# 入力ファイルパス (ex. "E:\Temp\Video\サンプル.ts")
#
# -g | --genre
# 番組のジャンル (ex. "ドラマ")
# 入力ファイルがあるディレクトリの下に {ジャンル} フォルダを
# 作成し、その下にファイルを移動する。
#
# -r | --renban
# ファイル名を連番にする
# -t と併用可（連番＋タイトルになる）
#
# -s | --series
# genre フォルダの下に、更に addkey フォルダを作成する
# 有効であった場合は "ドラマ\相棒\" や "アニメ\サザエさん\"
# といったフォルダを作成し、その下にファイルを移動する
#
# -t | --title
# ファイル名をいい感じのタイトル名に変更する
#

import os
import shutil
import argparse
import re


# 連番や話数を削除
def delete_episode_number(input_string):
    input_string = re.sub(r"^[＃\#][０１２３４５６７８９\d]+[　\s]*", "", input_string)
    input_string = re.sub(
        r"[　\s]+[＃\#][０１２３４５６７８９\d]+[　\s]*", "", input_string
    )
    input_string = re.sub(
        r"^第[０１２３４５６７８９零〇一二三四五六七八九十\d]+[回話集][　\s]*",
        "",
        input_string,
    )
    input_string = re.sub(
        r"[　\s]+第[０１２３４５６７８９零〇一二三四五六七八九十\d]+[回話集][　\s]*",
        "",
        input_string,
    )
    input_string = re.sub(
        r"^（[０１２３４５６７８９零〇一二三四五六七八九十\d]+）[　\s]*",
        "",
        input_string,
    )
    input_string = re.sub(
        r"[　\s]+（[０１２３４５６７８９零〇一二三四五六七八九十\d]+）[　\s]*",
        "",
        input_string,
    )
    return input_string


# ファイル名に付与する番号（連番）を抽出
def extract_episode_number(infile_name, outdir_path):
    # 全角と半角が混ざっていると面倒なのでひとまず半角にする
    infile_name = ztoh(infile_name)
    # 漢数字は数字に変更
    infile_name = kanji_to_number_conversion(infile_name)

    # ファイル名に #01 とかある場合
    match = re.search(r"\#[0]*(\d+)", infile_name)
    if match:
        return int(match.group(1))
    # ファイル名に 第○回 とか 第○話 がある場合
    match = re.search(r"第[0]*(\d+)[回話集]", infile_name)
    if match:
        return int(match.group(1))
    # ファイル名に (1) とかある場合
    match = re.search(r"（(\d+)）", infile_name)
    if match:
        return int(match.group(1))
    # タイトルから抽出できなかった時は出力先フォルダを参照して連番になるよう番号を決める。
    renban = 1
    try:
        if os.path.exists(outdir_path):
            os.chdir(outdir_path)
            for file in os.listdir():
                if re.search(r"\#(\d+)", file):
                    tmp = int(re.search(r"\#(\d+)", file).group(1)) + 1
                    renban = max(renban, tmp)
    except Exception:
        pass
    return renban


# ファイル名から副題っぽい部分を抽出する
def extract_subtitle(infile_name, addkey):
    # 副題は addkey の後ろにあると想定し前部分を排除
    if addkey:
        match = re.search(rf"{addkey}[」】！？～＞：　 \s]*(.+)", infile_name)
        if match:
            infile_name = match.group(1)

    # 話数が含まれていたら削除
    infile_name = delete_episode_number(infile_name)

    # 括弧があればその中身を副題として抜き出す
    match = re.search(r"[「【](.*)", infile_name)
    if match:
        tmp = match.group(1)
        # 括弧の後ろにさらに括弧があるケースを考慮
        if re.search(r"[「【](.*)", tmp):
            tmp = re.search(r"[「【](.*)", tmp).group(1)
        if re.search(r"([^」】]+)", tmp):
            return re.search(r"([^」】]+)", tmp).group(1)

    #  ：（コロン）／（スラッシュ） ▽ ▼があったらその後ろを副題として抜き出す
    match = re.search(r"[：／▽▼](.*)", infile_name)
    if match:
        return match.group(1)

    # 副題が抽出できなかった場合は addkey を副題とする
    return addkey if not infile_name else infile_name


# 保存ファイル名を決定する
def get_outfile_name(
    infile_name, addkey, outdir_path, title_mode, renban_mode, series_mode
):
    # 拡張子を取る
    infile_name = re.sub(r"\.ts$", "", infile_name)
    # ディスカバリーによくある "(二)" が邪魔なので消去
    infile_name = re.sub(r"\(二\)$", "", infile_name)
    # ディスカバリーで稀にある "(日)" も邪魔なので消去
    infile_name = re.sub(r"\(日\)$", "", infile_name)

    # 半角と全角が混ざっていると面倒なので半角にする
    infile_name = ztoh(infile_name)
    addkey = ztoh(addkey)

    # 記号はファイル名やフォルダ名前にも使える全角にする
    infile_name = safe_string(infile_name)
    addkey = safe_string(addkey)

    # ファイル名から副題を抽出
    title = ""
    if title_mode:
        title = extract_subtitle(infile_name, addkey)
        title = delete_episode_number(title)
        if not title:
            title = addkey

    # ファイル名から連番を抽出
    renban = 0
    if renban_mode:
        renban = extract_episode_number(infile_name, outdir_path)

    # 連番＋副題
    if renban and title:
        return f"#{renban:02d} {title}.ts"
    # 副題のみ
    if title:
        return f"{title}.ts"
    # 連番のみ
    if renban:
        return f"#{renban:02d}.ts"
    # どちらもない
    if series_mode and addkey:
        # addkey より前は重複するので排除
        match = re.search(rf"{addkey}[」】！？～＞：　 \s]*(.+)", infile_name)
        if match:
            infile_name = match.group(1)
    return f"{infile_name}.ts"


# 保存先ディレクトリパスを決定する
def get_outdir_path(path_to_store, genre, addkey, series):
    # ジャンルが指定されていたならディレクトリパスにジャンル名を追加
    if genre:
        path_to_store = os.path.join(path_to_store, genre)
    # シリーズフラグがあれば更に予約キーワード(addkey) を追加
    if series and addkey:
        addkey = ztoh(addkey)
        addkey = safe_string(addkey)
        path_to_store = os.path.join(path_to_store, addkey)
    return path_to_store


# 漢数字を半角数字に置換
def kanji_to_number_conversion(input_string):
    kanji_to_number = {
        "零": "0",
        "〇": "0",
        "一": "1",
        "二": "2",
        "三": "3",
        "四": "4",
        "五": "5",
        "六": "6",
        "七": "7",
        "八": "8",
        "九": "9",
        "十": "10",
    }
    for kanji, number in kanji_to_number.items():
        input_string = input_string.replace(kanji, number)
    return input_string


# ファイルを保存先に移動する
def move_file(infile_path, outdir_path, outfile_name):
    if not infile_path or not outdir_path or not outfile_name:
        return
    outfile_path = os.path.join(outdir_path, outfile_name)

    bakdir_path = os.path.join(outdir_path, "前回")
    bakfile_path = os.path.join(bakdir_path, outfile_name)
    bakbakdir_path = os.path.join(outdir_path, "前々回")
    bakbakfile_path = os.path.join(bakbakdir_path, outfile_name)

    # 入力ファイルが存在するか確認
    if not os.path.isfile(infile_path):
        return

    # 入力と出力が同じなら何もしない
    if infile_path == outfile_path:
        return

    try:
        # 出力先ディレクトリを作成
        os.makedirs(outdir_path, exist_ok=True)

        # 上書きになる場合はバックアップを取っておく
        if os.path.isfile(outfile_path):
            # バックアップディレクトリを作成
            os.makedirs(bakdir_path, exist_ok=True)
            # バックアップ
            if os.path.isfile(bakfile_path):
                os.makedirs(bakbakdir_path, exist_ok=True)
                shutil.move(bakfile_path, bakbakfile_path)
            shutil.move(outfile_path, bakfile_path)

        # 移動
        shutil.move(infile_path, outfile_path)
    except Exception:
        pass


# ジャンルフォルダの最終更新時刻を更新
def update_folder_utime(parent_dir, genre, series):
    if not parent_dir or not genre or not series:
        return
    # ダミーファイルを作成→削除してフォルダの utime を更新する
    dummyfile_path = os.path.join(parent_dir, genre, ".dummy")
    try:
        if os.path.exists(dummyfile_path):
            os.remove(dummyfile_path)
        with open(dummyfile_path, "w"):
            pass
        os.remove(dummyfile_path)
    except Exception:
        pass


# 半角の記号をファイルやフォルダ名に使える全角に変更
def safe_string(input_string):
    replacechars = {
        "(": "（",
        ")": "）",
        ":": "：",
        ";": "；",
        "/": "／",
        "\\": "￥",
        "|": "｜",
        ",": "，",
        "*": "＊",
        "-": "－",
        "~": "～",
        "?": "？",
        "!": "！",
        "&": "＆",
        '"': "”",
        "<": "＜",
        ">": "＞",
    }
    if input_string:
        for b, a in replacechars.items():
            input_string = input_string.replace(b, a)
    return input_string


# 全角（英数＋＃＋スペース）を半角に変更(ＡＢＣ　＃１２３ → ABC #123)
def ztoh(input_string):
    replacechars = {
        "Ａ": "A",
        "Ｂ": "B",
        "Ｃ": "C",
        "Ｄ": "D",
        "Ｅ": "E",
        "Ｆ": "F",
        "Ｇ": "G",
        "Ｈ": "H",
        "Ｉ": "I",
        "Ｊ": "J",
        "Ｋ": "K",
        "Ｌ": "L",
        "Ｍ": "M",
        "Ｎ": "N",
        "Ｏ": "O",
        "Ｐ": "P",
        "Ｑ": "Q",
        "Ｒ": "R",
        "Ｓ": "S",
        "Ｔ": "T",
        "Ｕ": "U",
        "Ｖ": "V",
        "Ｗ": "W",
        "Ｘ": "X",
        "Ｙ": "Y",
        "Ｚ": "Z",
        "ａ": "a",
        "ｂ": "b",
        "ｃ": "c",
        "ｄ": "d",
        "ｅ": "e",
        "ｆ": "f",
        "ｇ": "g",
        "ｈ": "h",
        "ｉ": "i",
        "ｊ": "j",
        "ｋ": "k",
        "ｌ": "l",
        "ｍ": "m",
        "ｎ": "n",
        "ｏ": "o",
        "ｐ": "p",
        "ｑ": "q",
        "ｒ": "r",
        "ｓ": "s",
        "ｔ": "t",
        "ｕ": "u",
        "ｖ": "v",
        "ｗ": "w",
        "ｘ": "x",
        "ｙ": "y",
        "ｚ": "z",
        "＃": "#",
        "♯": "#",
        "０": "0",
        "１": "1",
        "２": "2",
        "３": "3",
        "４": "4",
        "５": "5",
        "６": "6",
        "７": "7",
        "８": "8",
        "９": "9",
        "　": " ",
    }
    if input_string:
        for b, a in replacechars.items():
            input_string = input_string.replace(b, a)
        # 連続した空白は１つにまとめる
        input_string = re.sub(r"\s+", " ", input_string)
    return input_string


# メインルーチン
def main():
    parser = argparse.ArgumentParser(
        description="EDCB recording post-processing script."
    )
    parser.add_argument(
        "-a",
        "--addkey",
        type=str,
        help='Keyword used during reservation recording (e.g., "相棒")',
    )
    parser.add_argument("-d", "--debug", action="store_true", help="Debug mode")
    parser.add_argument(
        "-f",
        "--filepath",
        type=str,
        required=True,
        help='Input file path (e.g., "E:\\Temp\\Video\\サンプル.ts")',
    )
    parser.add_argument(
        "-g", "--genre", type=str, help='Program genre (e.g., "ドラマ")'
    )
    parser.add_argument(
        "-r", "--renban", action="store_true", help="Make the file name a serial number"
    )
    parser.add_argument(
        "-s",
        "--series",
        action="store_true",
        help="Create an addkey folder under the genre folder",
    )
    parser.add_argument(
        "-t",
        "--title",
        action="store_true",
        help="Change the file name to a nice title name",
    )

    args = parser.parse_args()

    # 録画ファイル名
    infile_name = os.path.basename(args.filepath)
    if not infile_name:
        return

    # 録画ファイルがあるディレクトリのパス
    parent_dir = os.path.dirname(args.filepath)
    if not parent_dir:
        return

    # ファイル名が Genre_TItle.ts という形式なのでジャンル部分とタイトル部分に分割
    genre = infile_name.split("_", 1)[0] if "_" in infile_name else ""
    title = infile_name.split("_", 1)[1] if "_" in infile_name else infile_name

    # ジャンル名を簡略化
    if "教養" in genre:
        genre = "教養"
    elif "アニメ" in genre:
        genre = "アニメ"

    # 保存先ディレクトリパス
    outdir_path = get_outdir_path(parent_dir, genre, args.addkey, args.series)
    if not outdir_path:
        return

    # 保存ファイル名
    outfile_name = get_outfile_name(
        title, args.addkey, outdir_path, args.title, args.renban, args.series
    )
    if not outfile_name:
        return

    # 保存先へ移動しジャンルフォルダの最終更新時刻を更新
    if not args.debug:
        move_file(args.filepath, outdir_path, outfile_name)
        update_folder_utime(parent_dir, args.genre, args.series)
    else:
        print("  " + outdir_path + "\\" + outfile_name)


# エントリーポイント
if __name__ == "__main__":
    main()

# EOF
