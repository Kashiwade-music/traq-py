#!/bin/sh

set -eux

usage_exit() {
  echo "Usage: ./upload.sh [-t]"
  echo "  -t: Upload to testpypi instead of pypi"
}

TEST=false

while getopts t OPT; do
  case $OPT in
  t) TEST=true ;;
  *) usage_exit ;;
  esac
done

cd ./out

# Build archive to upload
python3 -m pip install --upgrade build
python3 -m build

# Upload
if [ $TEST ]; then
  TARGET=testpypi
else
  TARGET=pypi
fi
python3 -m pip install --upgrade twine
python3 -m twine upload --repository "$TARGET" dist/*
