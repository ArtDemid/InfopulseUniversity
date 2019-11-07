import http.client
import json


class Book:
    base_url = "/books/"

    def __init__(self, title, author, id=None):
        self.title = title
        self.author = author
        self.id = id

    def url(self):
        return f"{self.base_url}/{self.id}"

    def to_dict(self):
        d = self.__dict__
        return {atr: d[atr] for atr in d if d[atr] is not None}

    def __str__(self):
        return f"{self.__class__}: title={self.title}, author={self.author}"


if __name__ == "__main__":
    b = Book("t", "a")
    print(b.to_dict())


class PulseTestAPI:
    def __init__(self, domain):
        self.domain = domain

    def _to_json_or_str(self, response_body):
        try:
            return json.loads(str(response_body))
        except json.decoder.JSONDecodeError:
            return str(response_body)

    def create(self, obj):
        con = http.client.HTTPConnection(self.domain)
        con.request("POST", obj.base_url, json.dumps(obj.to_dict()), {"Content-Type": "application/json"})
        response = con.getresponse()
        con.close()
        # TODO Try to understand next line:
        response.body = self._to_json_or_str(response.read())
        return response

    def delete(self, obj):
        con = http.client.HTTPConnection(self.domain)
        con.request("DELETE", obj.url(), "", headers={"Content-Type": "application/json"})
        response = con.getresponse()
        con.close()
        response.body = self._to_json_or_str(response.read())
        return response
