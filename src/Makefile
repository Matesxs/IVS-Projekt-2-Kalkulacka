init:
	pip install -r requirements.txt

doc:
	Doxygen Doxyfile

test:
	python library_tests.py

test_with_coverage:
	-coverage run library_tests.py
	coverage report -m