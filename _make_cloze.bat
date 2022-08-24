@echo off
cd source-cloze

set PATH=..\venv\Scripts;%PATH%
call activate.bat

python.exe _make-cloze.py
pause