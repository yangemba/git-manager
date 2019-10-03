import sys
import os
from os import system, getcwd
import argparse
import logging

url = 'https://github.com/yangemba/avrs-content-taker.git'
branch = 'ubuntu18'


def get_project_name():
    first = url.split('.git')[0]
    return first.split('/')[1]


def clone():
    os.system(f'git clone {url}')
    logging.warning(f"Cloning {url}")


def checkout():
    try:
        os.system(f'cd {str(os.getcwd()+"/"+ get_project_name())}')
        print(os.getcwd())
        os.system(f'git checkout {branch}')
        logging.warning(f"Checkout to {branch}")
    except Exception as e:
        logging.exception(f'There is no branch called <{branch}>')


clone()
checkout()






























