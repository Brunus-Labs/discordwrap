default:
    @just --list

build:
    @rm -rf build dist
    @echo "Removed cached files"
    @echo y | pip uninstall discordwrap
    @echo "Removed old lib"
    @poetry build
    @echo "Built lib"
    @poetry install
    @echo "Installed new lib"
