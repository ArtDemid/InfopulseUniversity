import json

class UrlProvider:

    base_url = "http://the-internet.herokuapp.com"

    def __init__(self):
        self._load_data()

    def _load_data(self):
        try:
            with open("url_test_data.json", "r") as _file:
                self.test_data = json.load(_file)
        except Exception as ex:
            return print("Exception occured while loading test data\n", ex)

    def get_test_url(self, _item = None):
        item = str(_item)
        if self.test_data:
            for i in self.test_data:
                if i['name'] == item:  
                    return self.base_url + i['url']