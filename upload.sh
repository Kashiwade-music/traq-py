#!/bin/sh

set -eux

cd ./out

python3 setup.py install

python3 -m pip install --upgrade twine
python3 -m twine upload --repository testpypi dist/*
