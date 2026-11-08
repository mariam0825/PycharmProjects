import uuid

class User:
    def __init__(self, name, username, password ):
        self.name = name
        self.username = username
        self.password = password
        self.id  = self.generate_id()

    def login(self, username, password):
        return self.username == username and self.password == password

    def generate_id(self):
       return str(uuid.uuid4())