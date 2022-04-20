import os
import xml.etree.ElementTree as ET

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


    def initialize(self, ctf_url=None, creds=None):
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
            if self.configured:
                raise ConfigException("Workspace Already Exists")
            self.ctf = StandardCTF()

            # logging messgae for creating standard worspace


        # logging about categories and about their no. of tasks

        for category in self.ctf.categories:
            os.makedirs(_WORKSPACE + category.name, exist_ok = True)

        # write worspace information to config file
        print(list(self.ctf.categories))
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
        config = ET.parse(_CONFIG_FILE_PATH).getroot()
        platform_cls = globals()[config.find('platform').text]
        return platform_cls.read_config(config)


    def write_config(self):
        self.ctf.convert_to_tree().write(_CONFIG_FILE_PATH)

