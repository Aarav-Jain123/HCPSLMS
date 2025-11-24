@echo off
REM Change to your project directory
cd /d C:\Users\Aarav Jain\Desktop\HCPSLMS 

REM Activate the Python virtual environment
call .venv\Scripts\activate

REM Start Django runserver
python manage.py runserver
