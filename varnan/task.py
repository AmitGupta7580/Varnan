class Task:
    def __init__(self, name, description, points = 0, attachments = [], solved = False, flag = None):
        self.name = name
        self.description = description
        self.points = points
        self.attachments = attachments
        self.solved = solved
        self.flag = flag

    def mark_solved(self, flag):
        self.solved = True
        self.flag = flag