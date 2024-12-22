@echo off

set RECPOST="%~dp0\RecPost.py"

set FILEPATH="D:\Videos\テレビ\放課後カルテ 最終回　卒業の涙…保健室去る牧野先生から子ども達へ最後の言葉.ts"
set ADDKEY="放課後カルテ"
set GENRE="ドラマ"
call :SubRoutine

set FILEPATH="D:\Videos\テレビ\今日から俺は!! #4 「大恋愛が加速！？先生どうして人を好きになるんですか？」.ts"
set ADDKEY="今日から俺は!!"
set GENRE="ドラマ"
call :SubRoutine

set FILEPATH="D:\Videos\テレビ\フラエジ「私をもらって～恋路編～」#4▼儚いラブストーリー第2章.ts"
set ADDKEY="私をもらって～恋路編～"
set GENRE="ドラマ"
call :SubRoutine

set FILEPATH="D:\Videos\テレビ\映像の世紀バタフライエフェクト　ナチ親衛隊　狂気の実行者たち.ts"
set ADDKEY="映像の世紀バタフライエフェクト"
set GENRE="教養"
call :SubRoutine

set FILEPATH="D:\Videos\テレビ\ＭＦゴースト　２ｎｄ　Ｓｅａｓｏｎ　★Ｔｕｒｎ２２「ザ・ペニンシュラ開幕」.ts"
set ADDKEY="MFゴースト"
set GENRE="アニメ"
call :SubRoutine

set FILEPATH="D:\Videos\テレビ\ブラタモリ　東海道“五十七次”の旅▼第三夜　ついにゴールの大阪へ！.ts"
set ADDKEY="ブラタモリ"
set GENRE="教養"
call :SubRoutine

set FILEPATH="D:\Videos\テレビ\＜木曜劇場＞わたしの宝物【最終回！托卵から始まった物語の結末は…】　＃１０.ts"
set ADDKEY="わたしの宝物"
set GENRE="ドラマ"
call :SubRoutine

set FILEPATH="D:\Videos\テレビ\金曜ドラマ「ライオンの隠れ家」　第１１話【僕たちの新しい始まり】.ts"
set ADDKEY="ライオンの隠れ家"
set GENRE="ドラマ"
call :SubRoutine

set FILEPATH="D:\Videos\テレビ\モンスター 最終決戦！環境汚染訴訟でリベンジマッチ！父親をぶっ潰せ！ ＃１０.ts"
set ADDKEY="モンスター"
set GENRE="ドラマ"
call :SubRoutine

set FILEPATH="D:\Videos\テレビ\ザ・トラベルナース ＃８.ts"
set ADDKEY="ザ・トラベルナース"
set GENRE="ドラマ"
call :SubRoutine

set FILEPATH="D:\Videos\テレビ\麒麟（きりん）がくる　（１２）「光秀、西へ」.ts"
set ADDKEY="麒麟（きりん）がくる"
set GENRE="ドラマ"
call :SubRoutine

set FILEPATH="D:\Videos\テレビ\とある科学の一方通行 #07.ts"
set ADDKEY="とある科学の一方通行"
set GENRE="アニメ"
call :SubRoutine

set FILEPATH="D:\Videos\テレビ\火曜ドラマ「Ｈｅａｖｅｎ？～ご苦楽レストラン～」♯７　常連客の知られざる秘密.ts"
set ADDKEY="Heaven?~ご苦楽レストラン~"
set GENRE="ドラマ"
call :SubRoutine

set FILEPATH="D:\Videos\テレビ\#17 夏休みのつづり.ts"
set ADDKEY="とある魔術の禁書目録Ⅲ"
set GENRE="アニメ"
call :SubRoutine

set FILEPATH="D:\Video\ハケン占い師アタル ＃３.ts"
set ADDKEY="ハケン占い師アタル"
set GENRE="ドラマ"
call :SubRoutine

set FILEPATH="D:\Video\火曜ドラマ「初めて恋をした日に読む話」 第３話【届け！俺のキモチ】.ts"
set ADDKEY="初めて恋をした日に読む話"
set GENRE="ドラマ"
call :SubRoutine

set FILEPATH="D:\Video\名車再生！クラシックカー・ディーラーズ：新コンビ舞台裏(二).ts"
set ADDKEY="名車再生"
set GENRE="趣味"
call :SubRoutine

set FILEPATH="D:\Videos\テレビ\３年Ａ組　－今から皆さんは、人質です－#04事件は核心へー。必見の第4話.ts"
set ADDKEY="3年A組 -今から皆さんは、人質です-"
set GENRE="ドラマ"
call :SubRoutine

set FILEPATH="D:\Video\ブラタモリ「＃１２４　福井」.ts"
set ADDKEY="ブラタモリ"
set GENRE="教養"
call :SubRoutine

set FILEPATH="D:\Video\ピアノの森（１４）「懸ける想い」.ts"
set ADDKEY="ピアノの森"
set GENRE="アニメ"
call :SubRoutine

set FILEPATH="D:\Video\家売るオンナの逆襲#05 偽装美女&野獣カップルに起死回生の家爆売りGO!.ts"
set ADDKEY="家売るオンナの逆襲"
set GENRE="ドラマ"
call :SubRoutine

set FILEPATH="D:\Video\ゲームセンターCX #258 やっぱり延長…「ロックマンX2」.ts"
set ADDKEY="ゲームセンターCX"
set GENRE="趣味"
call :SubRoutine

set FILEPATH="D:\Video\美の巨人たち 吉村芳生『新聞と自画像』超絶リアルな新聞…え！これ描いたもの？.ts"
set ADDKEY="美の巨人たち"
set GENRE="教養"
call :SubRoutine

set FILEPATH="D:\Video\コズミック フロント☆ＮＥＸＴ▽酸素誕生に迫れ！南極 氷の下のタイムカプセル.ts"
set ADDKEY="コズミックフロント"
set GENRE="教養"
call :SubRoutine

exit /b

rem ===============================================================================

:SubRoutine

echo ●ジャンル
%RECPOST% -f %FILEPATH% -g %GENRE% -s --debug

echo ●ジャンル＋シリーズ＋副題
%RECPOST% -f %FILEPATH% -a %ADDKEY% -g %GENRE% -s -t --debug

echo ●ジャンル＋シリーズ＋連番＋副題
%RECPOST% -f %FILEPATH% -a %ADDKEY% -g %GENRE% -s -t -r --debug

set /p stdin="type any key to continue>"
exit /b