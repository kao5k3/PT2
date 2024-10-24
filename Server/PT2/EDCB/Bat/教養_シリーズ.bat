@echo off

rem -f : 入力ファイルパス (ex. "D:\Video\入力ファイル.ts")
rem -g : ジャンル＝出力先フォルダ名 (ex. "ドラマ")
rem -a : 検索キーワード (ex. "相棒")
rem -s : 検索キーワードでサブフォルダ作成
rem -t : ファイル名をタイトルにする
rem -r : ファイル名を連番にする（-t と併用すると連番＋タイトルになる）

C:\PT2\EDCB\Bat\RecPost.pl -f "$FilePath$" -g "教養" -a "$AddKey$" -s
