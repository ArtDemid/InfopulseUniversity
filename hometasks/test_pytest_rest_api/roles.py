import json

class Role:
    
    base_url = "/roles/"

    def __init__(self, name=None, _type=None, level=None, book=None, id=None):
        self.name = name
        self.type = _type
        self.level = level
        self.book = book
        self.id = id

    def __str__(self):
        return f"{self.__class__}: name={self.name}, type={self.type}, level={self.level}, book={self.book}"

    def load_test_data(self):
        try:
            with open("role_test_data.json", "r") as _file:
                self.test_data = json.load(_file)
                return self.test_data
        except Exception as ex:
            return print("Exception occured while loading test data\n", ex)