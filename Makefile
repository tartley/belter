
ve=~/.virtualenvs/belter

virtualenv:
	python3.7 -m venv --clear ~/.virtualenvs/belter

install-deps:
	. ${ve}/bin/activate && pip install -U pip
	. ${ve}/bin/activate && pip install -Ur requirements-dev.txt

lint:
	flake8 belter

test:
	pytest belter

