@echo off
set PATH=venv\Scripts;%PATH%
call activate.bat

python.exe multichoice/_multichoice.py
pause