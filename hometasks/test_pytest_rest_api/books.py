import json

class Book:
    
    base_url = "/books/"

    def __init__(self, title=None, author=None, id=None):
        self.title = title
        self.author = author
        self.id = id

    def __str__(self):
        return f"{self.__class__}: title={self.title}, author={self.author}"

    def load_test_data(self):
        try:
            with open("book_test_data.json", "r") as _file:
                self.test_data = json.load(_file)
                return self.test_data
        except Exception as ex:
            return print("Exception occured while loading test data\n", ex)