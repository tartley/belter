ve=~/.virtualenvs/belter
bin=${ve}/bin
python=${bin}/python
pip=${bin}/pip
packages=${HOME}/.cache/pip/packages

virtualenv:
	if [ -n "${VIRTUAL_ENV}" ]; then \
		echo "deactivate virtualenv first"; \
	else \
		python3.7 -m venv --clear ${ve} ; \
		echo $(realpath .) >${ve}/.project ; \
		${pip} install -U pip ; \
	fi

update-deps:
	# create requirements/*.txt
	pip-compile -q --upgrade --output-file=requirements/main.txt setup.py
	pip-compile -q --upgrade --output-file=requirements/dev.txt setup.py requirements/dev.in

download:
	# Download packages to local cache.
	# 'dev.txt' should be a superset of 'main.txt'
	yes w | ${pip} download \
		--destination-directory ${packages} \
		-r requirements/dev.txt

wheel:
	# Convert downloaded packages into wheels
	${pip} install -U wheel
	${pip} wheel \
		--wheel-dir ${packages} \
		-r requirements/dev.txt

install:
	# Install (and uninstall) wheels from local cache.
	pip-sync \
		--no-index \
		--find-links=${packages} \
		requirements/dev.txt

update: update-deps download wheel install

lint:
	${python} -m flake8 belter

unit:
	${python} -m pytest -q --color=yes

test: lint unit

.SILENT:

.PHONY: virtualenv update-deps download wheel install update lint unit test

