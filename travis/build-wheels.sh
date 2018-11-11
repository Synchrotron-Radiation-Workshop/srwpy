#!/bin/bash
set -e -x

# Install a system package required by our library
yum install -y atlas-devel wget

pushd /io/core/
make all
popd

# Compile wheels
for PYBIN in /opt/python/*/bin; do
    # "${PYBIN}/pip" install -r /io/requirements.txt
    "${PYBIN}/pip" wheel /io/ -w wheelhouse/
done

# Bundle external shared libraries into the wheels
for whl in wheelhouse/srwpy*.whl; do
    auditwheel repair "$whl" -w /io/wheelhouse/
done

# Install packages and test
# for PYBIN in /opt/python/cp36-cp36m/bin/; do
#     "${PYBIN}/pip" install srwpy --no-index -f /io/wheelhouse
# done
