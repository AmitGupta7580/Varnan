from asyncio import Task
import time
from typing import overload
from varnan.category import Category


class CTF:
    def __init__(self, name, categories, url=None):
        self.name = name
        self.categories = categories
        self.url = url

    @classmethod
    def convert_to_tree(cls):
        '''
        Convert CTF class to XML Tree
        '''
        
        return None

    @classmethod
    def read_config(cls, config):
        '''
        Cast XML config file date into CTF inherited class
        '''

        return None



class StandardCTF(CTF):
    def __init__(self):
        '''
        Default Workspace

        Standard Workspace -> 
                Categories : 
                    1. Web
                    2. Crypto
                    3. Misc
                    4. Reversing
        '''
        self.categories = (Category(name) for name in ["Web", "Crypto", "Misc", "Reversing"])
        super().__init__(f"Unnamed_{int(time.time())}", self.categories)
    
