@echo off

rem -f : ���̓t�@�C���p�X (ex. "D:\Video\���̓t�@�C��.ts")
rem -g : �W���������o�͐�t�H���_�� (ex. "�h���}")
rem -a : �����L�[���[�h (ex. "���_")
rem -s : �����L�[���[�h�ŃT�u�t�H���_�쐬
rem -t : �t�@�C�������^�C�g���ɂ���
rem -r : �t�@�C������A�Ԃɂ���i-t �ƕ��p����ƘA�ԁ{�^�C�g���ɂȂ�j


rem C:\PT2\EDCB\Bat\RecPost.pl -f "$FilePath$" -g "�h���}" -a "$AddKey$"


rem �����L�[���[�h�̑���ɏt�ďH�~(ex. "23�N�t")�ŃT�u�t�H���_���쐬����
set y=%date:~2,2%
set m=%date:~5,2%
setlocal ENABLEDELAYEDEXPANSION
set q=�~
if %m%==04 (
	set q=�t
) else if %m%==05 (
	set q=�t
) else if %m%==06 (
	set q=�t
) else if %m%==07 (
	set q=��
) else if %m%==08 (
	set q=��
) else if %m%==09 (
	set q=��
) else if %m%==10 (
	set q=�H
) else if %m%==11 (
	set q=�H
) else if %m%==12 (
	set q=�H
)
C:\PT2\EDCB\Bat\RecPost.pl -f "$FilePath$" -g "�h���}" -a "!y!�N!q!" -s
ENDLOCAL
