
ve=~/.virtualenvs/belter
python=${ve}/bin/python

virtualenv:
	python3.7 -m venv --clear ${ve}

install-deps:
	${python} -m pip install -U pip
	${python} -m pip install -Ur requirements-dev.txt

lint: SHELL := /bin/bash
lint:
	${python} -m flake8 belter | colout '^([^:]+):([0-9]+):([0-9]+): ([^ ]+)' cyan,cyan,white,red normal,normal,dim ; ! (( $${PIPESTATUS[0]} ))

unit:
	${python} -m pytest -q --color=yes

test: lint unit

.SILENT:

.PHONY: virtualenv install-deps lint unit test

