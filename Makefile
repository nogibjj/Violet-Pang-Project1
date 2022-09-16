install: 
	pip install --upgrade pip &&\
		pip install -r reuqirements.txt

test: 
	python -m pytest -vv test_*.py 

format: 
	black *.py dblib/*py 

lint: 
	pylint --disable=R,C --ignore-patterns=test_.*?py *.py dblib

all: install lint test
