#!/bin/sh
cd /home/josh/github/discordwrap
rm -rf build dist
echo "Removed cached files\n"
echo y | pip uninstall discordwrap
echo "Removed old lib\n"
python -m build
echo "Built lib\n"
pip install dist/discordwrap-*.whl
echo "Installed new lib\n"
