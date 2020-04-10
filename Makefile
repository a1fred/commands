.PHONY: dist
dist:
	python3 setup.py sdist
	twine upload dist/*
	git tag `cat setup.py | grep VERSION | grep -v version | cut -d= -f2 | tr -d "[:space:]"`
	git push --tags
