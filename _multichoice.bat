@echo off
cd multichoice
set PATH=..\venv\Scripts;%PATH%
call activate.bat

python.exe _multichoice.py
pause