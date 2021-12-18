

.ONESHELL:
test:
	python -m unittest
format:
	source .env/bin/activate
	yapf --recursive --in-place tests
	yapf --recursive --in-place algos
summary:
	source .env/bin/activate
	coverage report -m
