#!/usr/bin/env bash

# This script repacks generated wheel for removing original source code and setup a proper name since binary compilation was

cd wheels

# single wheel
wheelfile=`ls *whl`

# unpack wheel and remove source code
unzip -o $wheelfile
rm -rf ttopt/ $wheelfile

metadatafile=`find . -iname WHEEL`

# generate a proper python triplet (see: https://packaging.python.org/en/latest/specifications/platform-compatibility-tags/)
# only up to 3.11 and only for CPython :)
python_triplet=`python -c 'import sys; import distutils; print("%s%i%i-abi3-%s" % ({"cpython":"cp"}[sys.implementation.name], sys.implementation.version.major, sys.implementation.version.minor, distutils.util.get_platform().replace("-","_").replace(" ","_")))'`

# patch necessary files and generate a proper filename
# Linux only!
sed -i "s/Tag:.*/Tag: ${python_triplet}/" $metadatafile
wheelname=`echo $wheelfile | rev | cut -d"-" -f4- | rev`
wheelfilename=`echo "${wheelname}-${python_triplet}.whl"`

# pack new wheel
zip ${wheelfilename} * -r9

cd ..
