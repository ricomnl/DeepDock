PROJECT_NAME = deepdock

.venv:
	poetry install

kernel: .venv
	poetry run python -m ipykernel install --user --name ${PROJECT_NAME}