#!/bin/bash

set -e

rm -f AIND-Recognizer.zip

rm -rf tmp
mkdir tmp

pushd tmp >> /dev/null

git clone git@github.com:luzi82/AIND-Recognizer.git
rm -rf AIND-Recognizer/.git

zip -r AIND-Recognizer.zip AIND-Recognizer
mv AIND-Recognizer.zip ../

popd >> /dev/null

rm -rf tmp

