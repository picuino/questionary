@echo off
set PATH=..\venv\Scripts;%PATH%
call activate.bat

cd multichoice
python.exe _multichoice.py
pause