@echo off
cd source-multichoice
set PATH=..\venv\Scripts;%PATH%
call activate.bat

python.exe _make-multichoice.py
pause