# VARIABLES
PYTHON_COMMAND = python manage.py

run:
	sudo docker compose up

down:
	sudo docker compose down

build:
	sudo docker compose build

app:
	django-admin startapp $(name)
	mv $(name) ./apps/
	sed -i 's/$(name)/apps.$(name)/g' ./apps/$(name)/apps.py

compile:
	rm -rf prod.txt
	rm -rf dev.txt
	rm -rf test.txt

	pip-compile requirements/prod.in
	pip-compile requirements/dev.in
	pip-compile requirements/test.in

migrations:
	sudo docker compose run app $(PYTHON_COMMAND) makemigrations

migrate:
	sudo docker compose run app $(PYTHON_COMMAND) migrate

bash:
	sudo docker exec -it django-studies-app-1 /bin/sh

shell:
	sudo docker compose run app $(PYTHON_COMMAND) shell