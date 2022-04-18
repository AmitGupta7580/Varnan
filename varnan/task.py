class Task:
    def __init__(self, name, description, points = 0, attachments = [], solved = False):
        self.name = name
        self.description = description
        self.points = points
        self.attachments = attachments
        self.solved = solved