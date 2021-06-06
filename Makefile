.PHONY: build
build:
	python3 setup.py sdist bdist_wheel

.PHONY: publish
publish: build
	python3 -m twine upload --repository-url https://upload.pypi.org/legacy/ dist/*
