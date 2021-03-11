class User:
    nextId = 1  # 2

    def __init__(self, name=""):
        self.name = name
        self.id = User.nextId
        User.nextId += 1
