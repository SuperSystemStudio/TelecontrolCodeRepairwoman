cd I:\TelecontrolCodeRepairwoman
rd /s/q dist
python setup.py sdist
twine upload dist/*
rd /s/q dist
pip uninstall Telecontrol
pip install Telecontrol