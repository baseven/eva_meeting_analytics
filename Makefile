install:
	pipenv install

process:
	pipenv run python src/main.py $(ARGS)

