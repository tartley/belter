ve=~/.virtualenvs/belter
bin=${ve}/bin
python=${bin}/python
pip=${bin}/pip
packages=~/.cache/pip/packages

virtualenv:
	# Create an empty virtualenv
	python3.7 -m venv --clear ${ve}
	# enable virtualenvwrapper 'workon'
	echo $(realpath .) >${ve}/.project
	${python} -m pip install -U pip

freeze:
	# Read latest requirements/*.in files
	${pip} install -Ur requirements/dev.in
	# Generate updated requirements/dev.txt file.
	chmod u+w requirements/dev.txt
	/bin/echo -e "# Generated file do not edit, see 'Makefile:freeze'\n" > requirements/dev.txt
	${pip} freeze >> requirements/dev.txt
	chmod a-w requirements/dev.txt

download:
	# Download packages to local cache.
	${pip} download --destination-directory ${packages} -r requirements/dev.txt
	# Convert into wheels if required.
	${pip} wheel --wheel-dir ${packages} -r requirements/dev.txt

install:
	# Install wheels from local cache.
	${python} -m pip install --no-index --find-links=${packages} -r requirements/dev.txt

setup: virtualenv freeze download install

repopulate: virtualenv install

lint:
	${python} -m flake8 belter

unit:
	${python} -m pytest -q --color=yes

test: lint unit

.SILENT:

.PHONY: virtualenv freeze download install setup repopulate lint unit test

