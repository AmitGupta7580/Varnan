class CTF:
    def __init__(self, name, categories, tasks=[], url=None):
        self.name = name
        self.categories = categories
        self.tasks = tasks
        self.url = url

    def convert_to_config(self):
        '''
        '''
        config = f"""name: {self.name}\ncategories: \
            """
        return config

    @classmethod
    def read_config(cls, config):
        '''
        '''
        name = "Unnnamed"
        categories = []
        return cls(name, categories)