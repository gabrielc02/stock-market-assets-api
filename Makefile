run:
	uvicorn app.main:app --reload

install:
	pip install -r requirements.txt

venv:
	python -m venv venv

activatevenv:
	env/Script/activate

test:
	pytest

lint:
	pylint app