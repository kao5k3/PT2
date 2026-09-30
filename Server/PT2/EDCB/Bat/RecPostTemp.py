#
# 説明
#
#  EDCB で録画後に実行するバッチプログラムから呼び出される Python スクリプト。
#
#  録画ファイル（＝TSファイル）を「アニメ\とあるシリーズ\とある科学の一方通行」
#  フォルダに移動する。
#
# 前提条件
#
#  * 入力ファイル名は  $Genre$_$Title$.ts 形式となるよう  RecNameMacro で設定
#    されていること
#
# 引数
#
# -f | --filepath
#  入力ファイルパス (ex. "E:\Temp\Video\サンプル.ts")
#

import argparse
import logging
import os
import re
import shutil

logger = logging.getLogger(__name__)


# 出力ファイル名を決定する
def get_outfile_name(infile_name):
    # 拡張子を取る
    infile_name = re.sub(r"\.ts$", "", infile_name)
    # ディスカバリーによくある "(二)" が邪魔なので消去
    infile_name = re.sub(r"\(二\)$", "", infile_name)
    # ディスカバリーで稀にある "(日)" も邪魔なので消去
    infile_name = re.sub(r"\(日\)$", "", infile_name)

    # 半角と全角が混ざっていると面倒なので全部半角にする
    infile_name = ztoh(infile_name)

    # 記号はファイルやフォルダ名にも使える全角にする
    infile_name = safe_string(infile_name)

    return f"{infile_name}.ts"


# 出力先ディレクトリパスを決定する
def get_outdir_path(parent_dir):
    return os.path.join(parent_dir, "アニメ", "とあるシリーズ", "とある科学の一方通行")


# ファイルを出力先に移動する
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
        logger.exception("ファイルの移動に失敗しました")

# Windowsでファイル名やフォルダ名に使えない半角記号+αを全角に変換
def safe_string(input_string):
    replacechars = {
        "<": "＜",
        ">": "＞",
        ":": "：",
        '"': "“",
        "/": "／",
        "\\": "￥",
        "|": "｜",
        "?": "？",
        "*": "＊",
        "~": "～",
        "!": "！",
        "-": "－",
    }
    if input_string:
        # "" で囲まれた文字列があれば前後の " を全角の “ ” に変換
        input_string = re.sub(r'"(.*?)"', r"“\1”", input_string)
        # その他は１文字単位で変換
        for b, a in replacechars.items():
            input_string = input_string.replace(b, a)
        # ！？ を ⁉ に置換
        input_string = input_string.replace("！？", "⁉")
        # ！！ を ‼ に置換
        input_string = input_string.replace("！！", "‼")
    return input_string


# 全角英数記号文字を半角に変更(ＡＢＣ　＃１２３ → ABC #123)
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
        "！": "!",
        "“": '"',
        "”": '"',
        "＃": "#",
        "♯": "#",
        "＄": "$",
        "％": "%",
        "＆": "&",
        "’": "'",
        "（": "(",
        "）": ")",
        "＊": "*",
        "＋": "+",
        "，": ",",
        "－": "-",
        "．": ".",
        "／": "/",
        "：": ":",
        "；": ";",
        "＜": "<",
        "＝": "=",
        "＞": ">",
        "？": "?",
        "＠": "@",
        "［": "[",
        "￥": "\\",
        "］": "]",
        "＾": "^",
        "＿": "_",
        "‘": "`",
        "｛": "{",
        "｜": "|",
        "｝": "}",
        "～": "~",
    }
    if input_string:
        for b, a in replacechars.items():
            input_string = input_string.replace(b, a)
        # 連続した空白は１つにまとめる
        input_string = re.sub(r"\s+", " ", input_string)
    return input_string


# メインルーチン
def main():
    parser = argparse.ArgumentParser(description="EDCB録画後処理スクリプト。")
    parser.add_argument(
        "-f",
        "--filepath",
        type=str,
        required=True,
        help='入力ファイルパス (例: "E:\\Temp\\Video\\サンプル.ts")',
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

    # ファイル名が Genre_Title.ts という形式なのでタイトル部分のみ取り出す
    title = infile_name.split("_", 1)[1] if "_" in infile_name else infile_name

    # 出力先ディレクトリパス
    outdir_path = get_outdir_path(parent_dir)
    if not outdir_path:
        return

    # 出力ファイル名
    outfile_name = get_outfile_name(title)
    if not outfile_name:
        return

    # 出力先へ移動
    move_file(args.filepath, outdir_path, outfile_name)

# エントリーポイント
if __name__ == "__main__":
    main()

# EOF
