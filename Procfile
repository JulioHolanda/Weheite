web: gunicorn dj_login_system.wsgi:aplication --log-file - --log-level debug
python manage.py collectstatic --noinput
manage.py migrate