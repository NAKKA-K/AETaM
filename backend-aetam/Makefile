.DEFAULT_GOAL := help

.PHONY: help run test migrate

help:
	@cat Makefile

run:
	python manage.py runserver

test:
	python -m unittest discover -s aetam/tests

migrate:
	python manage.py migrate
