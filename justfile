default:
    @just --list

build:
    @poetry build
    @echo "Built lib"
    @poetry install
    @echo "Installed new lib"

format:
    @poetry run black .

test: build
    @poetry run black --check .
    @poetry run pytest

get_payload: build
    @poetry run python scripts/get_payload.py
