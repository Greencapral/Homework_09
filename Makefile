test:
	poetry run pytest

server:
	python manage.py runserver

pylint:
	poetry run pylint $(shell git ls-files '*.py')

coverage:
	poetry run pytest --cov --cov-branch --cov-report=xml --cov-fail-under 20
	npx jest --coverage
