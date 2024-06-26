start:
	python3 manage.py runserver --settings=config.settings.dev

dev-install:
	pip install -r requirements/dev.txt

dev-m:
	python3 manage.py migrate --settings=config.settings.dev