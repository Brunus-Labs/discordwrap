default:
    @just --list

build:
    @poetry build
    @echo "Built lib"
    @poetry install
    @echo "Installed new lib"

test: build
    @poetry run pytest
