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
for re-run we have to do:
tox -r

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

# standard python coding guidelines 
PEP 8
we can use library flake8 for pep 8 testing


So now we create a web app and app.py file

Now we have to create directory as .github workflows for ci-cd 
mkdir -p .github/workflows

and create a file called ci-cd.yaml

Ingerating with heroku 
creating application dvc_project
to create authorization token click account settings and applications
get the token and then create secrets in github account
after adding the repo secret we need to create procfile
create procfile in root it is the entry point for heroku, heroku search for the Procfile to connect
to run application
so run command below to create procfile on the root directory
touch Procfile


