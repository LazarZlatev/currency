manage_py:=  python3 ./app/manage.py

run:
	$(manage_py) runserver 0.0.0.0:8000

migrations:
	$(manage_py) makemigrations

migrate:
	$(manage_py) migrate

shell:
	$(manage_py) shell_plus --print-sql

createsuperuser:
	$(manage_py) createsuperuser

flake:
	flake8 app/

worker:
	cd app && celery -A settings worker -l info --autoscale 1,10
