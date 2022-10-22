web: gunicorn dj_login_systemd.wsgi:aplication --log-file - --log-level debug
python manage.py collectstatic --noinput
manage.py migrate