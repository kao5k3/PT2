@echo off

rem -f : 入力ファイルパス (ex. "D:\Video\入力ファイル.ts")
rem -g : ジャンル＝出力先フォルダ名 (ex. "ドラマ")
rem -a : 検索キーワード (ex. "相棒")
rem -s : 検索キーワードでサブフォルダ作成
rem -t : ファイル名をタイトルにする
rem -r : ファイル名を連番にする（-t と併用すると連番＋タイトルになる）


rem C:\PT2\EDCB\Bat\RecPost.pl -f "$FilePath$" -g "ドラマ" -a "$AddKey$"


rem 検索キーワードの代わりに春夏秋冬(ex. "23年春")でサブフォルダを作成する
set y=%date:~2,2%
set m=%date:~5,2%
setlocal ENABLEDELAYEDEXPANSION
set q=冬
if %m%==04 (
	set q=春
) else if %m%==05 (
	set q=春
) else if %m%==06 (
	set q=春
) else if %m%==07 (
	set q=夏
) else if %m%==08 (
	set q=夏
) else if %m%==09 (
	set q=夏
) else if %m%==10 (
	set q=秋
) else if %m%==11 (
	set q=秋
) else if %m%==12 (
	set q=秋
)
C:\PT2\EDCB\Bat\RecPost.pl -f "$FilePath$" -g "ドラマ" -a "!y!年!q!" -s
ENDLOCAL
