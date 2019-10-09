import os
import argparse
import logging


class GitManager(object):
    """Class for managing git project"""

    def __init__(self, **kwargs):
        self.url = kwargs.get('url')
        self.commit = kwargs.get('commit')
        self.x_arg = kwargs.get('x_arg')

    def get_project_name(self):
        """Function for extracting project-name from link"""
        first = self.url.split('.git')[0]
        result = first.split('/')[-1]
        return result

    def clone(self) -> None:
        """Function for cloning remote repository"""
        os.system(f'git clone {self.url}')
        logging.warning(f"Cloning {self.url}")

    def checkout(self) -> None:
        """Function for choosing commit reference"""
        try:
            os.system(f'cd {str(os.getcwd()+"/"+ self.get_project_name())} '
                      f'&& git checkout {self.commit}')
        except Exception as e:
            logging.exception(f'There is no branch called <{self.commit}>')

    def execute(self):
        """Function for executing existing python
           file with injected argument"""
        file_names_list = os.listdir(path=str(os.getcwd()+'/' +
                                              self.get_project_name()))
        current_file = False
        for file_name in file_names_list:
            if '.py' in file_name:
                current_file = file_name
        os.system(f'cd {str(os.getcwd() + "/" + self.get_project_name())} '
                  f'&& python {current_file} -x {self.x_arg}')

    def clean_work_dir(self):
        """Function for cleaning current working directory"""
        os.system(f'rm -rf {self.get_project_name()}')

    def run(self):
        """Function for running settlement"""
        self.clone()
        self.checkout()
        self.execute()
        self.clean_work_dir()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--url", help="U")
    parser.add_argument("-c", "--commit", help="")
    parser.add_argument("-x", "--xarg", help="")
    args = parser.parse_args()
    url = args.url
    commit = args.commit
    x_arg = args.xarg
    git_manager_instance = GitManager(url=url,
                                      commit=commit,
                                      x_arg=x_arg)
    git_manager_instance.run()
