#!/bin/bash

git clean -fdx
pushd core/ && make all && popd && python setup.py sdist bdist_wheel && \
    twine upload dist/*
