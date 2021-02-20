@echo off
set PATH=venv\Scripts;%PATH%
call activate.bat

python.exe questionary.py
pause