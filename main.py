import sys
import os
from os import system, getcwd
import argparse
import logging

# url = 'https://github.com/yangemba/avrs-content-taker.git'
# branch = 'ubuntu18'


def get_project_name(url):
    first = url.split('.git')[0]
    logging.warning(f'first = {first}')
    result = first.split('/')[-1]
    logging.warning(f'result = <{result}> + type {type(result)} + len '
                    f'{len(result)}')
    return result


def clone(link: str) -> None:
    os.system(f'git clone {link}')
    logging.warning(f"Cloning {link}")


def checkout(name, work_tree) -> None:
    try:
        os.system(f'cd {str(os.getcwd()+"/"+ name)} && git '
                  f'checkout {branch}')
        logging.warning(f"Checkout to {work_tree}")
    except Exception as e:
        logging.exception(f'There is no branch called <{work_tree}>')


def execute(name, x_number):
    file_name = os.listdir(path=str(os.getcwd()+'/'+name))[0]
    os.system(f'cd {str(os.getcwd() + "/" + name)} && python {file_name} -x '
              f'{x_number}')
    pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--url", help="U")
    parser.add_argument("-b", "--branch", help="")
    parser.add_argument("-x", "--xarg", help="")
    args = parser.parse_args()

    url = args.url
    branch = args.branch
    x_args = args.xarg
    project_name = get_project_name(url)
    clone(url)
    checkout(url, branch)
































