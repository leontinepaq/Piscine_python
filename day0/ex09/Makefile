VENV = .venv
PYTHON = $(VENV)/bin/python
PIP = $(VENV)/bin/pip

.PHONY: all clean build install test

all: clean venv build install test

venv:
	python3 -m venv $(VENV)
	$(PIP) install --upgrade pip build

build:
	$(PYTHON) -m build

install:
	$(PIP) install dist/*.whl

test:
	for f in tests/test_*.py; do $(PYTHON) $$f; done

clean:
	rm -rf $(VENV) dist build *.egg-info
