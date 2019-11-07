import unittest
import requests


class BookTests(unittest.TestCase):
    def setUp(self):
        self.base_url = "http://pulse-rest-testing.herokuapp.com/"
        self.books = [  # TODO: read data from file
            {"title": "1234", "author": "I"},
            {"title": "1234", "author": "I"},
            {"title": "1234", "author": "I"}
        ]

    def test_book_create(self):
        for book in self.books:
            with self.subTest(book):
                response = requests.post(self.base_url+"books/", data=book)
                self.assertEqual(response.status_code, 201)
                resp_dict = response.json()
                # for key in book:
                #     self.assertEqual(resp_dict[key], book[key])
                book["id"] = resp_dict["id"]
                self.assertDictEqual(book, resp_dict)

    def tearDown(self):
        for book in self.books:
            if "id" in book:
                requests.delete(self.base_url + 'books/{}/'.format(book["id"]))



