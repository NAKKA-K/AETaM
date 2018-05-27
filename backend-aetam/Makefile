.DEFAULT_GOAL := help

.PHONY: help install run test migrate

help:
	@cat Makefile

install:
	pip install -r requirements.txt

run:
	python manage.py runserver

test:
	python -Wall -m unittest discover -s aetam/tests

migrate:
	python manage.py migrate
