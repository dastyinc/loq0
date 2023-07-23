rm -rf dist/
cd loq0
python3 setup.py sdist
mv dist/ ../dist/
rm -rf build/ dist/ loq0.egg-info/
cd ..
twine upload dist/*