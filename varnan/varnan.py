import os
import xml.etree.ElementTree as ET
from varnan.category import Category

from varnan.exceptions import ConfigException
from varnan.ctf import StandardCTF

class Varnan:
    global _WORKSPACE, _CONFIG_FILE_PATH
    _WORKSPACE = os.getcwd() + '\\'
    _CONFIG_FILE_PATH = _WORKSPACE + '.varnan_config.xml'

    def __init__(self):
        '''
        Initialization of Varnan Class
        '''

        # Workspace Information
        self.configured = os.path.exists(_CONFIG_FILE_PATH)

        # fetch configuration of tool from working directory
        if self.configured:
            self.ctf = self.read_config()


    def initialize(self, ctf_name, ctf_url=None, creds=None):
        '''
        Initialize Standard/Customized Workspace
        '''
        if ctf_url:
            # fetch platform information from ctf_url and get the class for that platform
            # self.ctf = cls()

            # check the creds on that platform

            # extract the information of the ctf
            # self.categories = []
            
            # logging message for creating standard worspace

            pass
        else:
            self.ctf = StandardCTF(ctf_name)

            # logging messgae for creating standard worspace


        # logging about categories and about their no. of tasks

        for category in self.ctf.categories:
            os.makedirs(_WORKSPACE + category.name, exist_ok = True)

        # write worspace information to config file
        self.write_config()


    def link(self, ctf_url, creds):
        '''
        '''
        
        pass


    def show_stats(self):
        '''
        '''
        pass
    

    def list_category(self):
        '''
        List all the present CTF Categories in the workspace
        '''
        print("Categories : ")
        for idx, category in enumerate(self.ctf.categories):
            print(f"\t{idx+1}. {category.name}")


    def list_task(self):
        '''
        List all the present CTF Tasks in the workspace.
        '''
        tasks_cnt, solved_tasks_cnt = 0, 0
        print("Tasks : ")
        for idx, category in enumerate(self.ctf.categories):
            print(f"\t{idx+1}. {category.name}")
            if len(category.tasks) == 0:
                print("\t\tNo Tasks")
            for idxx, task in enumerate(category.tasks):
                tasks_cnt += 1
                solved_tasks_cnt += 1 if task.solved else 0
                print(f"\t\t{idxx+1}. {task.name}")


    def add_category(self, category):
        '''
        Add CTF Category in the workspace
        '''
        self.ctf.categories.append(category)
        os.makedirs(_WORKSPACE + category.name, exist_ok = True)
        self.write_config()


    def add_task(self, task, category_name):
        '''
        Add CTF Task in the workspace
        '''
        category_exists = False
        for idx, category in enumerate(self.ctf.categories):
            if category.name == category_name:
                category_exists = True
                self.ctf.categories[idx].tasks.append(task)
        
        if not category_exists:
            # create category and add task into that
            self.ctf.categories.append(Category(category_name, tasks=[task]))
            os.makedirs(_WORKSPACE + category_name, exist_ok = True)

        # generation of Task files
        # files

        self.write_config()


    def solve_task(self, task_name, category_name, flag):
        '''
        Mark a Task as solved
        '''
        for idx, category in enumerate(self.ctf.categories):
            if category.name == category_name:
                for idxx, task in enumerate(category.tasks):
                    if task.name == task_name:
                        self.ctf.categories[idx].tasks[idxx].solved = True
                else:
                    print(f"No such task fount in {category.name} category")
        else:
            print("No such category found")

        self.write_config()


    def generate(self):
        '''
        '''

        pass


    def push_writup(self):
        '''
        '''

        pass


    def push(self):
        '''
        '''

        pass


    def read_config(self):
        '''
        Read config file from workspace and store all the \
        CTF information in inherited CTF class object
        '''
        config = ET.parse(_CONFIG_FILE_PATH).getroot()
        platform_cls = globals()[config.find('platform').text]
        return platform_cls.read_config(config)


    def write_config(self):
        '''
        Write the information of CTF from inherited CTF class object to a config file
        '''
        self.ctf.convert_to_tree().write(_CONFIG_FILE_PATH)

