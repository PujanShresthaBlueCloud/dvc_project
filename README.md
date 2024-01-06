# dvc_project
https://github.com/c17hawke/simple-dvc-demo/tree/main
create template.py and run it
tnen create data_given folder for dataset source
followed the remaining steps from git hub repo
create get_data file inside src folder
create load_data and update the dvc.yaml file witht the stages
run below command for dvc update dataset
dvc repro

install tox
create tox.ini file 
create tests folder and create file conftest.py and test_config.py and __init__.py
for test alway define test_ at first as prefix
to run test we can do pytest -v 
or we can do tox 

now create setup.py to create package 
and install -e so that all the local requirements are then installed in the package and install the package
pip install -e . 

check the package install by running 
pip freeze

we can see the information of package in src.egg-info

we can also share the package in tar file by running sdist is standard distribution and bdist is build distribution
python setup.py sdist bdist_wheel
so we can share the tar file inside dist folder to install the library

Range in the our data source case for good wine testing
we install the jupyterlab
pip install jupyterlab

then to open jupyter notebook we run the command below:
jupyter-lab notebooks/

then we copy the NotInRange class to test_config.py file for testing
then we do pytest -v to check


