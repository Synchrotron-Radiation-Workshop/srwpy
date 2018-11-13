@echo on

git clean -fdx

cd core
call make.bat
cd ..
python setup.py bdist_wheel
twine upload dist/*
