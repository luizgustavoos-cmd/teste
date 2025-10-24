@echo off
cd /d "C:\Users\Luiz Gustavo\Desktop\teste"
call env\Scripts\activate.bat
cd universe_project
start http://127.0.0.1:8000
python manage.py runserver
pause
