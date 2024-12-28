@echo off

set RECPOST="%~dp0\RecPost.py"

set FILEPATH="D:\Videos\テレビ\ドラマ_放課後カルテ 最終回　卒業の涙…保健室去る牧野先生から子ども達へ最後の言葉.ts"
set ADDKEY="放課後カルテ"
call :SubRoutine

set FILEPATH="D:\Videos\テレビ\ドラマ_今日から俺は!! #4 「大恋愛が加速！？先生どうして人を好きになるんですか？」.ts"
set ADDKEY="今日から俺は!!"
call :SubRoutine

set FILEPATH="D:\Videos\テレビ\ドラマ_フラエジ「私をもらって～恋路編～」#4▼儚いラブストーリー第2章.ts"
set ADDKEY="私をもらって～恋路編～"
call :SubRoutine

set FILEPATH="D:\Videos\テレビ\ドキュメンタリー／教養_映像の世紀バタフライエフェクト　ナチ親衛隊　狂気の実行者たち.ts"
set ADDKEY="映像の世紀バタフライエフェクト"
call :SubRoutine

set FILEPATH="D:\Videos\テレビ\アニメ／特撮_ＭＦゴースト　２ｎｄ　Ｓｅａｓｏｎ　★Ｔｕｒｎ２２「ザ・ペニンシュラ開幕」.ts"
set ADDKEY="MFゴースト"
call :SubRoutine

set FILEPATH="D:\Videos\テレビ\ドキュメンタリー／教養_ブラタモリ　東海道“五十七次”の旅▼第三夜　ついにゴールの大阪へ！.ts"
set ADDKEY="ブラタモリ"
call :SubRoutine

set FILEPATH="D:\Videos\テレビ\＜木曜劇場＞わたしの宝物【最終回！托卵から始まった物語の結末は…】　＃１０.ts"
set ADDKEY="わたしの宝物"
call :SubRoutine

set FILEPATH="D:\Videos\テレビ\ドラマ_金曜ドラマ「ライオンの隠れ家」　第１１話【僕たちの新しい始まり】.ts"
set ADDKEY="ライオンの隠れ家"
call :SubRoutine

set FILEPATH="D:\Videos\テレビ\ドラマ_モンスター 最終決戦！環境汚染訴訟でリベンジマッチ！父親をぶっ潰せ！ ＃１０.ts"
set ADDKEY="モンスター"
call :SubRoutine

set FILEPATH="D:\Videos\テレビ\ドラマ_ザ・トラベルナース ＃８.ts"
set ADDKEY="ザ・トラベルナース"
call :SubRoutine

set FILEPATH="D:\Videos\テレビ\ドラマ_麒麟（きりん）がくる　（１２）「光秀、西へ」.ts"
set ADDKEY="麒麟（きりん）がくる"
call :SubRoutine

set FILEPATH="D:\Videos\テレビ\アニメ／特撮_とある科学の一方通行 #07.ts"
set ADDKEY="とある科学の一方通行"
call :SubRoutine

set FILEPATH="D:\Videos\テレビ\ドラマ_火曜ドラマ「Ｈｅａｖｅｎ？～ご苦楽レストラン～」♯７　常連客の知られざる秘密.ts"
set ADDKEY="Heaven?~ご苦楽レストラン~"
call :SubRoutine

set FILEPATH="D:\Videos\テレビ\アニメ／特撮_#17 夏休みのつづり.ts"
set ADDKEY="とある魔術の禁書目録Ⅲ"
call :SubRoutine

set FILEPATH="D:\Video\ドラマ_ハケン占い師アタル ＃３.ts"
set ADDKEY="ハケン占い師アタル"
call :SubRoutine

set FILEPATH="D:\Video\ドラマ_火曜ドラマ「初めて恋をした日に読む話」 第３話【届け！俺のキモチ】.ts"
set ADDKEY="初めて恋をした日に読む話"
call :SubRoutine

set FILEPATH="D:\Video\趣味_名車再生！クラシックカー・ディーラーズ：新コンビ舞台裏(二).ts"
set ADDKEY="名車再生"
call :SubRoutine

set FILEPATH="D:\Videos\テレビ\ドラマ_３年Ａ組　－今から皆さんは、人質です－#04事件は核心へー。必見の第4話.ts"
set ADDKEY="3年A組 -今から皆さんは、人質です-"
call :SubRoutine

set FILEPATH="D:\Video\ドキュメンタリー／教養_ブラタモリ「＃１２４　福井」.ts"
set ADDKEY="ブラタモリ"
call :SubRoutine

set FILEPATH="D:\Video\アニメ／特撮_ピアノの森（１４）「懸ける想い」.ts"
set ADDKEY="ピアノの森"
call :SubRoutine

set FILEPATH="D:\Video\ドラマ_家売るオンナの逆襲#05 偽装美女&野獣カップルに起死回生の家爆売りGO!.ts"
set ADDKEY="家売るオンナの逆襲"
call :SubRoutine

set FILEPATH="D:\Video\趣味_ゲームセンターCX #258 やっぱり延長…「ロックマンX2」.ts"
set ADDKEY="ゲームセンターCX"
call :SubRoutine

set FILEPATH="D:\Video\ドキュメンタリー／教養_美の巨人たち 吉村芳生『新聞と自画像』超絶リアルな新聞…え！これ描いたもの？.ts"
set ADDKEY="美の巨人たち"
call :SubRoutine

set FILEPATH="D:\Video\ドキュメンタリー／教養_コズミック フロント☆ＮＥＸＴ▽酸素誕生に迫れ！南極 氷の下のタイムカプセル.ts"
set ADDKEY="コズミックフロント"
call :SubRoutine

exit /b

rem ===============================================================================

:SubRoutine

echo ●%FILEPATH%
echo  なし
%RECPOST% -f %FILEPATH% -a %ADDKEY% --debug

echo  シリーズ
%RECPOST% -f %FILEPATH% -a %ADDKEY% -s --debug

echo  シリーズ＋副題
%RECPOST% -f %FILEPATH% -a %ADDKEY% -s -t --debug

echo  シリーズ＋連番＋副題
%RECPOST% -f %FILEPATH% -a %ADDKEY% -s -t -r --debug

rem echo  シリーズ＋連番＋副題withGPT
rem %RECPOST% -f %FILEPATH% -a %ADDKEY% -s -t -r -g --debug

set /p stdin="type any key to continue>"
exit /b