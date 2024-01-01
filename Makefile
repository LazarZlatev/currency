manage_py:=  python3 ./app/manage.py

run:
	$(manage_py) runserver 0.0.0.0:8000

migrations:
	$(manage_py) makemigrations currency

migrate:
	$(manage_py) migrate currency

shell:
	$(manage_py) shell_plus --print-sql

createsuperuser:
	$(manage_py) createsuperuser

flake:
	flake8 app/
