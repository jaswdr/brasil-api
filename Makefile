build:
	python3 setup.py sdist bdist_wheel

publish: build
	python3 -m twine upload --repository-url https://upload.pypi.org/legacy/ dist/*
