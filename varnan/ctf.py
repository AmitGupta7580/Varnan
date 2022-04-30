import xml.etree.ElementTree as ET

from varnan.category import Category
from varnan.task import Task


class CTF:
    def __init__(self, name, categories, url=None):
        """
        Base Class for All CTF Platforms
        """
        self.name = name
        self.categories = categories
        self.url = url

    def convert_to_tree(self, platform_name):
        """
        Convert CTF class to XML Tree
        """
        # platform_name = fetch from cls
        config = ET.Element("varnan_config")
        platform_config = ET.SubElement(config, "platform")
        platform_config.text = platform_name
        ctf_name_config = ET.SubElement(config, "name")
        ctf_name_config.text = self.name
        for category in self.categories:
            category_config = ET.SubElement(config, "category")
            category_name_config = ET.SubElement(category_config, "name")
            category_name_config.text = category.name
            for task in category.tasks:
                task_config = ET.SubElement(category_config, "task")
                task_name_config = ET.SubElement(task_config, "name")
                task_name_config.text = task.name
                task_desc_config = ET.SubElement(task_config, "description")
                task_desc_config.text = task.description

                # optional parameters
                task_solved_config = ET.SubElement(task_config, "solved")
                task_solved_config.text = str(task.solved)
                task_points_config = ET.SubElement(task_config, "points")
                task_points_config.text = str(task.points)

                for attachment in task.attachments:
                    attachment_config = ET.SubElement(task_config, "attachment")
                    attachment_config.text = attachment
        return ET.ElementTree(config)

    @classmethod
    def read_config(cls, config):
        """
        Cast XML config file date into CTF inherited class
        """
        ctf_name = config.find("name").text
        categories = []
        for category_config in config.findall("category"):
            tasks = []
            category_name = category_config.find("name").text
            for task_config in category_config.findall("task"):

                task_name = task_config.find("name").text
                task_desc = task_config.find("description").text
                task = Task(task_name, task_desc)

                # task optional parameters
                if task_config.find("solved") is not None:
                    task.solved = task_config.find("solved").text == "True"
                if task_config.find("points") is not None:
                    task.points = int(task_config.find("points").text)

                # attachments
                attachments = []
                for attachment_config in task_config.findall("attachment"):
                    attachments.append(attachment_config.text)

                tasks.append(task)
            categories.append(Category(category_name, tasks))
        return cls(ctf_name, categories)


class StandardCTF(CTF):
    def __init__(self, name, categories=[]):
        """
        Default Workspace

        Standard Workspace ->
                Categories :
                    1. Web
                    2. Crypto
                    3. Misc
                    4. Reversing
        """
        self.name = name
        self.categories = (
            [Category(name) for name in ["Web", "Crypto", "Misc", "Reversing"]]
            if len(categories) == 0
            else categories
        )
        super().__init__(self.name, self.categories)

    def convert_to_tree(self):
        """
        Convert CTF class to XML Tree
        """
        return super().convert_to_tree("StandardCTF")
