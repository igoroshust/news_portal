# Commands to start a project:
1. python -m venv venv
2. venv\scripts\activate
3. pip install -r requirements.txt
4. cd project
5. python manage.py runserver

# Clear cache:
1. ctrl+shift+R
2. ctrl+F5

# Login/logout :
1. Sign up: http://127.0.0.1:8000/accounts/signup/
2. Sign in: http://127.0.0.1:8000/accounts/login/
3. Log Out: http://127.0.0.1:8000/accounts/logout/

# Delete news from the selected category:
1. cd projects
2. python manage.py delnews

# Email newsletter:
1. download redis: https://github.com/microsoftarchive/redis/releases
2. start redis-server.exe (run as administartor)
3. Terminal - Local (1): python manage.py runserver
4. Terminal - Local (2): celery -A project worker -l INFO --pool=solo

~~ Terminal - Local (2) can use: celery -A project worker -l INFO -P eventlet
5. Terminal - Local (3): celery -A project beat -l INFO
