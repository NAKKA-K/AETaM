.DEFAULT_GOAL := help

.PHONY: help vagrant/*

help:
	@cat Makefile

vagrant/up:
	vagrant up

vagrant/ssh:
	vagrant ssh

vagrant/destroy:
	vagrant destroy
