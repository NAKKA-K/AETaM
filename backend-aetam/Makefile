.DEFAULT_GOAL := help

.PHONY: help install run test migrate clean

PYTHON   = python
PIP      = pip
MANAGE   = manage.py
DATABASE = aetam.sqlite3


help: Makefile
	@cat Makefile

install:
	$(PIP) install -r requirements.txt

run: $(DATABASE)
	$(PYTHON) $(MANAGE) runserver

test:
	-$(PYTHON) -Wall -m unittest discover -s aetam/tests

migrate: $(DATABASE)
$(DATABASE):
	$(PYTHON) $(MANAGE) migrate

clean:
	-@rm $(DATABASE)
