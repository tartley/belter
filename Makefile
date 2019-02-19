ve=~/.virtualenvs/belter
bin=${ve}/bin
python=${bin}/python
activate=${bin}/activate
pip=${bin}/pip
packages=~/.cache/pip/packages

virtualenv:
	python3.7 -m venv --clear ${ve}
	# enable virtualenvwrapper 'workon'
	echo $(realpath .) >${ve}/.project
	${python} -m pip install -U pip

freeze:
	${pip} install -Ur requirements/dev.in
	chmod u+w requirements/dev.txt
	/bin/echo -e "# Generated file do not edit, see 'Makefile:freeze'\n" > requirements/dev.txt
	${pip} freeze >> requirements/dev.txt
	chmod a-w requirements/dev.txt

download:
	${pip} download --destination-directory ${packages} -r requirements/dev.txt
	${pip} wheel --wheel-dir ${packages} -r requirements/dev.txt

install:
	${python} -m pip install --no-index --find-links=${packages} -r requirements/dev.txt

repopulate: virtualenv install

setup: virtualenv download install

lint: SHELL := /bin/bash
lint:
	. ${activate} ; flake8 belter | colout '^([^:]+):([0-9]+):([0-9]+): ([^ ]+)' cyan,cyan,white,red normal,normal,dim ; ! (( $${PIPESTATUS[0]} ))

unit:
	${python} -m pytest -q --color=yes

test: lint unit

.SILENT:

.PHONY: virtualenv download install repopulate setup lint unit test

