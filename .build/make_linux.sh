#!/bin/bash

git clean -fdx
docker run --rm -v `pwd`:/io quay.io/pypa/manylinux1_x86_64 /io/travis/build-wheels.sh && \
    twine upload wheelhouse/*
