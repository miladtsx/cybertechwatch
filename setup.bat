@echo off
prompt #

echo. & echo installing docx module & echo.
python.exe -m pip install python-docx & echo.


echo. & echo installing feedparsed module & echo.
python.exe -m pip install feedparser & echo.

echo. & echo installing dateutil module & echo.
python.exe -m pip install python-dateutil & echo.

echo @echo off > run.bat
echo python.exe main.py >> run.bat


echo Done. & echo. & echo Now execute run.bat
prompt
