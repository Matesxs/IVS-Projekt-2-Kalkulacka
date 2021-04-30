.PHONY: all run init docs test test_with_coverage clean build build_standalone build_installer
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
	python utils/remove.py ".coverage"

clean:
	python utils/remove.py "..\docs"
	python utils/remove.py "..\install"
	python utils/remove.py "build"
	python utils/remove.py "dist"
	python utils/remove.py "Calculator.spec"
	python utils/remove.py ".coverage"

build: build_standalone build_installer

build_standalone:
	pyinstaller --onefile --noconsole --clean -n CalculatorStandalone main.py
	python utils/create_folder.py "..\install"
	copy dist\CalculatorStandalone.exe ..\install\CalculatorStandalone.exe
	python utils/remove.py "build"
	python utils/remove.py "dist"
	python utils/remove.py "CalculatorStandalone.spec"

build_installer:
	pyinstaller --onedir --noconsole --clean -n Calculator main.py
	python utils/create_folder.py "..\install"
	-iscc .\utils\installer_compile_script.iss
	python utils/remove.py "build"
	python utils/remove.py "dist"
	python utils/remove.py "Calculator.spec"