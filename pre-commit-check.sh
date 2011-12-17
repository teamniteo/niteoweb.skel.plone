#!/bin/bash

echo 'Running tests'
bin/py setup.py test

echo '====== Running ZPTLint ======'
for pt in `find src/niteoweb/zulu/ -name "*.pt"` ; do bin/zptlint $pt; done

echo '====== Running PyFlakes ======'
bin/pyflakes src/niteoweb/zulu
bin/pyflakes setup.py
bin/pep8 fabfile.py

echo '====== Running pep8 =========='
bin/pep8 src/niteoweb/zulu
bin/pep8 setup.py
bin/pep8 fabfile.py

