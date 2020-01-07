class User:
    def __init__(self, username="", password="", full_name="", email="", is_admin=False):
        self.username = username
        self.password = password
        self.full_name = full_name
        self.email = email
        self.is_admin = is_admin

    def __str__(self):
        return f"{self.__class__} object: username = {self.username}, password={self.password}"
    
    def __eq__(self, other):
        if self.username == "" or other.username == "":
            return self.full_name == other.full_name
        return self.username == other.username and self.full_name == other.full_name