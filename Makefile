.DEFAULT_GOAL := help

.PHONY: help run build clean

help:
	@cat Makefile

run:
	npm start

build:
	npm build

clean:
	rm -rf build


.PHONY: vagrant/*
vagrant/up:
	vagrant up

vagrant/ssh:
	vagrant ssh

vagrant/destroy:
	vagrant destroy
