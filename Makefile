
ve=~/.virtualenvs/belter

virtualenv:
	python3.7 -m venv ~/.virtualenvs/belter

install-deps:
	. ${ve}/bin/activate && pip install -U pip
	. ${ve}/bin/activate && pip install -Ur requirements-dev.txt

lint:
	. ${ve}/bin/activate && pylint belter

