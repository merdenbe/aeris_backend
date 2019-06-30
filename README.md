# aris_backend

### Basic setup (required)

#### Prerequisites
1. Python >=3.6
2. PostgreSQL

#### Install application

Install `virtualenv` for Python:

    $ pip3 install virtualenv

Create a virtual environment:

    $ virtualenv -p /usr/local/bin/python3 venv

Initialize environment variables from `env.sh`:

    $ source env.sh

Make sure that your virtual environment is using *Python >=3.6*:

    (venv) $ python --version
    Python 3.6.3
    ...

Install PIP dependencies (make sure you are inside your virtual environment!):

    (venv) $ pip install -r requirements.txt

### Start it all up

    Open a terminal instance and run the following:
    Note: theron should be running as well

        $ source env.sh
        (venv) $ gunicorn -b localhost:8001 --reload start:api
