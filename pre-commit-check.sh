#!/bin/bash

echo 'Running tests'
bin/test -s niteoweb.zulu

echo '====== Running ZPTLint ======'
for pt in `find src/niteoweb/zulu/ -name "*.pt"` ; do bin/zptlint $pt; done

echo '====== Running PyFlakes ======'
bin/zopepy setup.py flakes

echo '====== Running pep8 =========='
bin/pep8 --ignore=E501 src/niteoweb/zulu
bin/pep8 --ignore=E501 setup.py
bin/pep8 --ignore=E501 fabfile.py
