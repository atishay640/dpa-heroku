### Project Setup:
1. python3 -m vene env
2. source env/bin/activate
3. source .env-dev
4. python manage.py migrate
5. python manage.py createsuperuser


### Project execution:
1. python manage.py runserver
2. celery -A dpa worker -l info -c 6
3. celery -A dpa beat -l info
