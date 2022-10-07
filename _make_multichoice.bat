@echo off
cd source-multichoice
set PATH=..\venv\Scripts;%PATH%
call activate.bat

python.exe _make_multichoice.py
python.exe _make_multichoice_combine.py
pause