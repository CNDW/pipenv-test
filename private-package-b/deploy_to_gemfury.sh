#!/usr/bin/env bash
if [ ! -s VERSION ]; then
  echo "No version number specified. Not deploying."
  exit 0
fi
echo -n "Version number: "
cat VERSION
rm -rf dist

python setup.py sdist
if [ $? -eq 111 ]
then
    echo "found no tags to publish python package for, exiting gracefully"
    exit 0
fi
pip install --upgrade twine
twine upload --repository-url https://pypi.fury.io/cndw/ --username "${GEMFURY_WRITE_TOKEN}" --password "" dist/*  # token is in username in encrypted travis env var
