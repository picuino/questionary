@echo off
cd source-cloze

set PATH=..\venv\Scripts;%PATH%
call activate.bat

python.exe _make_cloze.py
pause