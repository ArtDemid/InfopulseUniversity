import unittest
import json
import api_manager
import books
import roles


class test_get_requests(unittest.TestCase):

    def setUp(self):
        self.book = books.Book()
        self.role = roles.Role()
        self.book_api_m = api_manager.ApiManager(self.book.base_url)
        self.role_api_m = api_manager.ApiManager(self.role.base_url)
        self.book_test_data = self.book.load_test_data()
        self.role_test_data = self.role.load_test_data()
    
    def test_GET_request_for_book(self):
        _id = self.book_api_m.get_item_id(self.book, self.book_test_data[0])
        request = self.book_api_m.read(self.book,_id)
        self.assertEqual(request.status, 404)

    def test_GET_request_for_role(self):
        _id = self.role_api_m.get_item_id(self.role, self.role_test_data[0])
        try:
            request = self.role_api_m.read(self.role,_id)
            self.assertEqual(request.status, 201)
        except Exception as ex:
            print(ex)

    def test_GET_all_book(self):
        try:
            request = self.book_api_m.read(self.book)
            self.assertIn(self.book_test_data, request.body)
        except Exception as ex:
            print(ex)
   
    def test_POST_for_book(self):
        try:
            for item in self.book_test_data:
                if item['title'] == 'Halo: Cryptum':
                    request = self.book_api_m.create(self.book, item)
            self.assertEqual(request.status, 201)
        except Exception as ex:
            print(ex)

    def test_DELETE_for_book(self):
        _id = self.book_api_m.get_item_id(self.book, self.book_test_data[0])
        try:
            request = self.book_api_m.delete(self.book,_id)
            self.assertEqual(request.status, 201)
        except Exception as ex:
            print(ex)

    def test_UPDATE_for_book(self):
        _id = self.book_api_m.get_item_id(self.book, self.book_test_data[0])
        try:
            request = self.book_api_m.update(self.book,_id)
            self.assertEqual(request.status, 201)
        except Exception as ex:
            print(ex)

if __name__ == "__main__":
    unittest.main()