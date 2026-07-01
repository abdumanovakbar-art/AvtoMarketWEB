dj:
	python manage.py runserver
mig:
	python manage.py makemigrations
	python manage.py migrate
ps:
	pip install psycopg2-binary

admin:
	 python manage.py createsuperuser


app:
	python manage.py startapp apps
