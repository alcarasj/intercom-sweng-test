test:
	pytest --cov-config=.coveragerc --cov=. . --cov-report=html

run:
	python3 main.py -i=./customers.txt -o=./output.txt 