#!/usr/bin/env make

# Version of Python
PYTHON ?= python3

# To define targets in each directory under the src/
define FOREACH
	for DIR in src/*; do \
		$(MAKE) -C $$DIR $(1); \
	done
endef

# ---------------------------------------------------------
# Setup a venv and install packages.
#

run: main.py
	@printf "This run the Game of Pig\n"
	$(PYTHON) src/DiceGame/main.py

version:
	@printf "Currently using executable: $(PYTHON)\n"
	which $(PYTHON)
	$(PYTHON) --version


install: requirements.txt
	$(PYTHON) -m pip install -r requirements.txt

installed:
	$(PYTHON) -m pip list

# Metrics
coverage:
	$(PYTHON) -m coverage run -m unittest discover src/DiceGame/
	coverage report
	coverage html

flake8:
	for f in src/DiceGame/*.py ; do flake8 $${f} ; done

pylint:
	for f in src/DiceGame/*.py; do \
		if grep -q test_ "$${f}"; then \
			continue; \
		else \
			pylint $${f}; \
		fi \
	done


# Documentation
doc:
	pdoc --html ${CURDIR}/src/DiceGame/*.py --output-dir ${CURDIR}/src/DiceGame/doc/html


# UML
uml:
	pyreverse src/DiceGame/*.py -a1 -s1
	dot -Tpdf ${CURDIR}/classes.dot -o ${CURDIR}/src/DiceGame/doc/uml/pig_game.pdf

# Clean Up
clean:
	@printf "This clean any files generated\n"
	@printf "by the coverage UML and documentation\n"
	rm -f .coverage *.pyc
	rm -f src/.coverage *.pyc
	rm -f src/DiceGame/.coverage src/DiceGame/*.pyc
	rm -f *.dot
	rm -f src/DiceGame/*.dot
	rm -rf src/DiceGame/__pycache__
	rm -rf htmlcov
	rm -rf src/DiceGame/doc/api/html
	rm -rf src/DiceGame/doc/uml

