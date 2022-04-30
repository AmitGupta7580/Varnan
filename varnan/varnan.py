import os
import shutil
import xml.etree.ElementTree as ET

from varnan.category import Category
from varnan.ctf import StandardCTF


class Varnan:
    global _WORKSPACE, _CONFIG_FILE_PATH
    _WORKSPACE = os.getcwd() + "\\"
    _CONFIG_FILE_PATH = _WORKSPACE + ".varnan_config.xml"

    def __init__(self):
        """
        Initialization of Varnan Class
        """
        self.ctf = None
        self.configured = False

    def initialize(self, ctf_name, ctf_url=None, creds=None):
        """
        Initialize Standard/Customized Workspace
        """
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
            print(f"[+] StandardCTF Workspace initialized")

    def link(self, ctf_url, creds):
        """ """
        pass

    def show_stats(self):
        """
        Show your progress in the CTF
        """
        print("[+] Statistics : \n  Categories : ")

        total_solved_tasks, total_tasks_cnt, total_points = 0, 0, 0
        for category in self.ctf.categories:
            solved_tasks, tasks_cnt, points = 0, len(category.tasks), 0
            for task in category.tasks:
                solved_tasks += 1 if task.solved else 0
                points += task.points if task.solved else 0
            total_solved_tasks += solved_tasks
            total_tasks_cnt += tasks_cnt
            total_points += points

            print(
                f"    |- {category.name} [{solved_tasks}/{tasks_cnt}] - {points} points"
            )

        print(
            f"Total Solved Tasks : [{total_solved_tasks}/{total_tasks_cnt}]\nTotal Points : {total_points}"
        )

    def list_category(self):
        """
        List all the present CTF Categories in the workspace
        """
        print("[+] Categories : ")
        for category in self.ctf.categories:
            print(f"  |- {category.name}")

    def add_category(self, category):
        """
        Add CTF Category in the workspace
        """
        for cat in self.ctf.categories:
            if cat.name == category.name:
                print("[-] Category already Exists")
                print("[!] First delete the category to recreate it.")
                return
        self.ctf.categories.append(category)

    def remove_category(self, category):
        """
        Remove CTF Category in the workspace
        """
        category_found = False
        for idx, cat in enumerate(self.ctf.categories):
            if cat.name == category.name:
                category_found = True
                self.ctf.categories.pop(idx)
                break

        if not category_found:
            print("[-] No such category found")

    def list_task(self):
        """
        List all the present CTF Tasks in the workspace.
        """
        tasks_cnt, solved_tasks_cnt = 0, 0
        print("[+] Tasks : ")
        for category in self.ctf.categories:
            print(f"  |- {category.name}")
            if len(category.tasks) == 0:
                print("     |- No Tasks")
            for task in category.tasks:
                tasks_cnt += 1
                solved_tasks_cnt += 1 if task.solved else 0
                print(f"     |- {task.name}")

    def add_task(self, task, category_name):
        """
        Add CTF Task in the workspace
        """
        category_exists = False
        for idx, category in enumerate(self.ctf.categories):
            if category.name == category_name:
                category_exists = True
                self.ctf.categories[idx].tasks.append(task)
                break

        if not category_exists:
            # create category and add task into that
            self.ctf.categories.append(Category(category_name, tasks=[task]))

    def remove_task(self, category_name, task_name):
        """
        Remove CTF Task in the workspace
        """
        category_found = False

        for idx, category in enumerate(self.ctf.categories):
            if category.name == category_name:
                category_found = True
                task_found = False

                for idxx, task in enumerate(category.tasks):
                    if task.name == task_name:
                        task_found = True
                        self.ctf.categories[idx].tasks.pop(idxx)
                        break

                if not task_found:
                    print(f"[-] No such task found in {category.name} category")
                    break

        if not category_found:
            print("[-] No such category found")

        self.write_config()

    def solve_task(self, task_name, category_name, flag):
        """
        Mark a Task as solved
        """
        category_found = False

        for idx, category in enumerate(self.ctf.categories):
            if category.name == category_name:
                category_found = True
                task_found = False

                for idxx, task in enumerate(category.tasks):
                    if task.name == task_name:
                        task_found = True
                        self.ctf.categories[idx].tasks[idxx].solved = True

                if not task_found:
                    print(f"[-] No such task found in {category.name} category")

        if not category_found:
            print("[-] No such category found")

    def generate(self):
        """ """

        pass

    def push_writup(self):
        """ """

        pass

    def push(self):
        """ """

        pass

    def update_workspace(self):
        """
        Update directories and files according to the ctf tasks and categories
        """

        all_categories = [
            name
            for name in os.listdir(_WORKSPACE)
            if os.path.isdir(os.path.join(_WORKSPACE, name))
        ]

        for category in self.ctf.categories:
            if not os.path.exists(_WORKSPACE + category.name):
                # create category directory
                os.makedirs(_WORKSPACE + category.name, exist_ok=True)
                print(f"[+] {category.name} category is successfully added")
            else:
                all_categories.remove(category.name)

            for task in category.tasks:
                # create task files for newly added task
                # print(f"[+] {task.name} is successfully added to {category.name}")
                continue

            # remove unwanted tasks

        # remove nwanted categories
        for category in all_categories:
            shutil.rmtree(_WORKSPACE + category)

    def read_config(self):
        """
        Read config file from workspace and store all the \
        CTF information in inherited CTF class object
        """
        config = ET.parse(_CONFIG_FILE_PATH).getroot()
        platform_cls = globals()[config.find("platform").text]
        return platform_cls.read_config(config)

    def write_config(self):
        """
        Write the information of CTF from inherited CTF class object to a config file
        """
        self.ctf.convert_to_tree().write(_CONFIG_FILE_PATH)
