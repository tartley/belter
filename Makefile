
ve=~/.virtualenvs/belter
python=${ve}/bin/python

virtualenv:
	python3.7 -m venv --clear ${ve}

install-deps:
	${python} -m pip install -U pip
	${python} -m pip install -Ur requirements-dev.txt

lint:
	${python} -m flake8 belter

unit:
	${python} -m pytest

test: lint unit

