~~ Commands to start a project ~~:
python -m venv venv
venv\scripts\activate
pip install -r requirements.txt
cd project
python manage.py runserver

~~ Clear cache ~~:
ctrl+shift+R
ctrl+F5

~~ Login/logout ~~:
Sign up: http://127.0.0.1:8000/accounts/signup/
Sign in: http://127.0.0.1:8000/accounts/login/
Log Out: http://127.0.0.1:8000/accounts/logout/

~~ Email newsletter ~~:
download redis: https://github.com/microsoftarchive/redis/releases
start redis-server.exe (run as administartor)
Terminal - Local (1): python manage.py runserver
Terminal - Local (2): celery -A project worker -l INFO --pool=solo
# Terminal - Local (2) can use: celery -A project worker -l INFO -P eventlet
Terminal - Local (3): celery -A project beat -l INFO
