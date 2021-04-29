.PHONY: all run init docs test test_with_coverage clean

all: init run

run:
	python main.py

init:
	pip install -r requirements.txt

doc:
	Doxygen Doxyfile

test:
	python library_tests.py

test_with_coverage:
	-coverage run library_tests.py
	coverage report -m

clean:
	@del .coverage