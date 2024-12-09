@echo off

:: Перейдем в директорию проекта
cd /d F:\Pycharm\Makarchan-Web-Interface

:: Активируем виртуальное окружение
call .venv\scripts\activate.bat

:: Запустим первый экземпляр uvicorn
start uvicorn main:app --host 0.0.0.0 --port 80