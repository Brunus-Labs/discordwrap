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
