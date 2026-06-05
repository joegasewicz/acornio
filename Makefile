test:
	poetry run pytest -vvvv

lint:
	poetry run pylint bobtail

docs:
	make -C docs html

install:
	poetry install
	poetry install --dev

# Tox is only for local development (we use github actions in CI)
tox:
	poetry run tox

release:
	poetry run python setup.py sdist
	poetry run twine upload dist/* --verbose