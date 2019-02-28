ve=~/.virtualenvs/belter
bin=${ve}/bin
python=${bin}/python
pip=${bin}/pip
packages=~/.cache/pip/packages

virtualenv:
	if [ -n "${VIRTUAL_ENV}" ]; then \
		echo "deactivate virtualenv first"; \
	else \
		python3.7 -m venv --clear ${ve} ; \
		echo $(realpath .) >${ve}/.project ; \
		${python} -m pip install -U pip ; \
	fi

download:
	# Download packages to local cache.
	yes w | ${pip} download --destination-directory ${packages} -r requirements/dev.in
	# Convert into wheels if required.
	${python} -m pip install -U wheel
	${pip} wheel --wheel-dir ${packages} -r requirements/dev.in

upgrade:
	# Install updated wheels from local cache.
	${python} -m pip install --no-index --find-links=${packages} -r requirements/dev.in

freeze:
	# Generate updated requirements/dev.txt file.
	chmod u+w requirements/dev.txt
	/bin/echo -e "# Generated file do not edit, see 'Makefile:freeze'\n" > requirements/dev.txt
	${pip} freeze >> requirements/dev.txt
	chmod a-w requirements/dev.txt
	#
	# This step is buggy, in that for packages specified as a git repo,
	# it puts the setup.py's 'version' param into requirements/dev.txt.
	# It should instead preserve the git repo url.
	# So after running 'freeze', manually repair these in the output. :-(
	echo ""
	git diff -U0 requirements/dev.txt
	echo ""
	echo "Now restore git repo urls in requirements/dev.txt"
	echo " * py2d"
	echo " * colout"
	echo ""

install:
	# Install pinned wheels from local cache.
	${python} -m pip install --no-index --find-links=${packages} -r requirements/dev.txt

setup: virtualenv freeze download install

repopulate: virtualenv install

lint:
	${python} -m flake8 belter

unit:
	${python} -m pytest -q --color=yes

test:
	./test

.SILENT:

.PHONY: virtualenv freeze download install setup repopulate lint unit test

