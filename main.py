import sys
import os
from os import system, getcwd
import argparse
import logging


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
    file_names_list = os.listdir(path=str(os.getcwd()+'/'+name))
    for file_name in file_names_list:
        if '.py' in file_name:
            current_file = file_name
    os.system(f'cd {str(os.getcwd() + "/" + name)} && python'
              f' {current_file} -x {x_number}')


def clean_work_dir(project_name):
    os.system(f'rm -rf {project_name}')


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
    checkout(project_name, branch)
    execute(project_name, x_args)
    clean_work_dir(project_name)

































