import json
import http.client
import urllib
import books
import roles
import time

class ApiManager:

    def __init__(self, isinstance_base_url):
        self.api_base_url = "pulse-rest-testing.herokuapp.com"
        self._connection = http.client.HTTPConnection(self.api_base_url)
    
    def _dispose(self):
        self._connection.close()
    
    def _to_json_or_str(self, response_body):
        try:
            return json.loads(str(response_body))
        except json.decoder.JSONDecodeError:
            return str(response_body)

    def get_item_id(self, instance, test_data):
        try:
            requset_url = instance.base_url
            self._connection.request("GET", requset_url)
            response = self._connection.getresponse()
            response.body = self._to_json_or_str(response.read().decode())
            self._dispose()
            # Внимание Костыль
            if type(instance) == type(books.Book()):
                if response.body:
                    for item in response.body:
                        if test_data['title'] == item['title']:
                            return item['id']
            elif type(instance) == type(roles.Role()):
                if response.body:
                    for item in response.body:               
                        if test_data['book'] == item['book']:
                            return item['id']
            else:
                return None
        except Exception as ex:
            return str(ex)

    def create(self, instance, data):
        if "id" in data:
            try:
                request_url = instance.base_url + data['id']
                params = urllib.parse.urlencode(data)
                self._connection.request("POST", request_url, params, {"Content-Type":"application/x-www-form-urlencoded"})
            except Exception as ex:
                return str(ex)
        else:
            try:
                request_url = instance.base_url
                params = urllib.parse.urlencode(data)
                self._connection.request("POST", request_url, params, {"Content-Type":"application/x-www-form-urlencoded"})
            except Exception as ex:
                return str(ex)
        
        response = self._connection.getresponse()
        response.body = self._to_json_or_str(response.read())
        self._dispose()
        if response.body:
            return response
        else:
            return None
    
    def read(self, instance, _id=None):
        if _id != None:
            request_url = instance.base_url + str(_id)
            self._connection.request("GET", request_url)
        else:
            request_url = instance.base_url
            self._connection.request("GET", request_url)
        
        response = self._connection.getresponse()
        response.body = self._to_json_or_str(response.read())
        self._dispose()
        if response.body:
            return response
        else:
            return None

    def update(self, instance, test_data, _id=None):
        if _id != None:
            try:
                request_url = instance.base_url + str(_id)
                params = urllib.parse.urlencode(test_data)
                self._connection.request("PUT", request_url, params, {"Content-Type":"application/x-www-form-urlencoded"})
            except Exception as ex:
                return str(ex)
        else:
            return None
        
        response = self._connection.getresponse()
        response.body = self._to_json_or_str(response.read())
        self._dispose()
        if response.body:
            return response
        else:
            return None

    def delete(self, instance, _id=None):
        if _id != None:
            try:
                request_url = instance.base_url + str(_id)
                self._connection.request("DELETE", request_url, "", {"Content-Type":"application/x-www-form-urlencoded"})
            except Exception as ex:
                return str(ex)
        else:
            return None
        
        response = self._connection.getresponse()
        response.body = self._to_json_or_str(response.read())
        self._dispose()
        if response.body:
            return response
        else:
            return None

#if __name__ == "__main__":
#    book = books.Book()
#    api_m = ApiManager(book.base_url)
#    test_data = book.load_test_data()
    #for item in test_data:
    #    print(item, sep="\n")
    #    if item['title'] == 'Halo: Cryptum':
    #        api_m.create(book, item)
#    for i in range(5):
#        _id = api_m.get_item_id(book, test_data[1])
    #read_by_id = api_m.read(book,_id)
    #read_all = api_m.read(book)
    #changed = api_m.update(book, test_data[1], _id)
#        api_m.delete(book, _id)
#        time.sleep(2)
#    print("Pause")
    
        
    
