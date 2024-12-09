:: Возвращаемся в корневую директорию
cd /d F:\Pycharm\Makarchan

:: Активируем виртуальное окружение
call .venv\scripts\activate.bat

:: Запустим второй экземпляр uvicorn
start uvicorn main:app --host 0.0.0.0 --port 8888