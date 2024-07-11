start:
	python3 manage.py runserver --settings=config.settings.dev

dev-install:
	pip install -r requirements/dev.txt

dev-m:
	python3 manage.py migrate reader zero --settings=config.settings.dev

dev-makem:
	python3 manage.py makemigrations --settings=config.settings.dev

dev-showm:
	python3 manage.py showmigrations --settings=config.settings.dev

dev-sqlm: 
	python3 manage.py sqlmigrate $(a) $(m) --settings=config.settings.dev

dev-dbshell:
	python3 manage.py dbshell --settings=config.settings.dev

dev-shell:
	python3 manage.py shell --settings=config.settings.dev