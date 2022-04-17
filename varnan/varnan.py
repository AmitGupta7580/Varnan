import os
from time import time

from varnan.category import Category
from varnan.exceptions import ConfigException
from varnan.task import Task
from varnan.ctf import CTF

class Varnan:
    def __init__(self):
        '''
        Initialization of Varnan Class
        '''

        self.workspace = os.getcwd() + '\\'

        # Workspace Information
        self.configured = os.path.exists(self.workspace + '.varnan.config')

        # fetch configuration of tool from working directory
        if self.configured:
            self.ctf = self.read_config()


    def initialize(self, ctf_url=None, creds=None):
        '''
        Initialize Standard/Customized Workspace

        Standard Workspace -> 
            Categories : 
                1. Web
                2. Crypto
                3. Misc
                4. Reversing
        '''
        
        if ctf_url:
            # extract the categories in the ctf
            # self.categories = []
            # construct self.ctf from ctf_url
            pass
        else:
            if self.configured:
                raise ConfigException("Workspace Already Exists")
            self.categories = ["Web", "Crypto", "Misc", "Reversing"]
            self.ctf = CTF(f"Unnamed_{int(time())}", self.categories)

        for category in self.categories:
            os.makedirs(self.workspace + category, exist_ok = True)

        # write worspace information to config file
        self.write_config()


    def link(self, ctf_url, creds):
        '''
        '''
        
        pass
    

    def list_category(self):
        '''
        '''
        
        pass


    def list_task(self):
        '''
        '''

        pass


    def add_category(self, category):
        '''
        '''

        pass


    def add_task(self, task):
        '''
        '''

        pass


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
        with open(self.workspace + '.varnan.config', 'r') as config_file:
            self.ctf = CTF.read_config(config_file.read())


    def write_config(self):
        with open(self.workspace + '.varnan.config', 'w') as config_file:
            config_file.write(self.ctf.convert_to_config())

