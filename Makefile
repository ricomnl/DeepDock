PROJECT_NAME = deepdock

.venv:
	poetry install
	git submodule update --init --recursive

kernel: .venv
	poetry run python -m ipykernel install --user --name ${PROJECT_NAME}

