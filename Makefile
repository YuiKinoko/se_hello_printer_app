deps:
	pip install -r requirements.txt; \
	pip install -r test_requirements.txt

lint:
	flake8 hello_world test

run:
	python main.py

.PHONY: test
test:
	PYTHONPATH=. py.test

docker_build:
	docker build -t hello-world-printer .