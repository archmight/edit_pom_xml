import os
import shutil
from os import path
import platform


class CreatingRepository:
    def __init__(self, jars_directory: str, project_path: str, directory_name="jars_dependencies"):

        self.jars_directory = jars_directory
        self.project_path = project_path

        self.directory_name = directory_name
        self.local_repo_path = os.path.join(self.project_path, self.directory_name)

        self.jars_list = []
        self.is_repo_exist_flag = False

        self.path_split_char = self.set_path_split_char()

    def mkdir_repository(self):
        """create directory. Check if it was created, set flag"""
        if not path.exists(self.local_repo_path):
            os.mkdir(self.local_repo_path)
        else:
            print("!! local repo exist, it will check on duplicates")
            self.is_repo_exist_flag = True

    def find_cp_and_set_jars_list(self):
        """call 2 methods find jars in directory and add all finded files  in local repo"""
        lst = self.find_jars()
        self.cp_jars(lst)

    def find_jars(self):
        """ recursively find all jar files"""
        paths_list = list()
        for root, dirs, files in os.walk(self.jars_directory):
            for file in files:
                if file.endswith(".jar"):
                    paths_list.append(os.path.join(root, file))
        return paths_list

    def cp_jars(self, jars_list: list):
        """copy in local repo only unique files"""


        if self.is_repo_exist_flag:
            current_files = os.listdir(os.path.join(self.project_path, self.directory_name))
            for jar_path in jars_list:
                if jar_path.split(self.path_split_char)[-1] in current_files:
                    print(jar_path.split(self.path_split_char)[-1] + " was added later")
                else:
                    shutil.copy(jar_path, os.path.join(self.project_path, self.directory_name))
                    print(jar_path.split(self.path_split_char)[-1] + ": ADDED IN LOCAL REPO")
                    self.jars_list.append(str(jar_path.split(self.path_split_char)[-1]))
        else:
            for jar_path in jars_list:
                shutil.copy(jar_path, os.path.join(self.project_path, self.directory_name))
                print(jar_path.split(self.path_split_char)[-1] + ": ADDED IN LOCAL REPO")
                self.jars_list.append(str(jar_path.split(self.path_split_char)[-1]))

    def set_split_char(self):
        self.path_split_char = self.set_path_split_char()

    def set_path_split_char(self):
        """method to correctly """
        if platform.system() == 'Windows':
            return '\\'
        elif platform.system() == 'Linux':
            return '/'
        else:
            print("WAIT FOR ERROR(class creating_repository, method set_path_split_char): not defined os.name=" + platform.system())