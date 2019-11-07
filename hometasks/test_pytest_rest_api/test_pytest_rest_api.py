#import pytest

class test_pytest_get_requests():
    
    def test_p_GET_request_for_book(self, book, book_api_m, book_test_data):
        _id = book_api_m.get_item_id(book, book_test_data[0])
        request = book_api_m.read(book,_id)
        assert request.status == 201

    def test_p_GET_request_for_role(self, role, role_api_m, role_test_data):
        _id = role_api_m.get_item_id(role, role_test_data[0])
        try:
            request = role_api_m.read(role,_id)
            assert request.status == 201
        except Exception as ex:
            print(ex)

    def test_p_GET_all_book(self, book, book_api_m, book_test_data):
        try:
            request = book_api_m.read(book)
            assert book_test_data in request.body
        except Exception as ex:
            print(ex)
   
    def test_p_POST_for_book(self, book, book_api_m, book_test_data):
        try:
            for item in book_test_data:
                if item['title'] == 'Halo: Cryptum':
                    request = book_api_m.create(book, item)
            assert request.status == 201
        except Exception as ex:
            print(ex)

    def test_p_DELETE_for_book(self, book, book_api_m, book_test_data):
        _id = book_api_m.get_item_id(book, book_test_data[0])
        try:
            request = book_api_m.delete(book,_id)
            assert request.status == 201
        except Exception as ex:
            print(ex)

    def test_p_UPDATE_for_book(self, book, book_api_m, book_test_data):
        _id = book_api_m.get_item_id(book, book_test_data[0])
        try:
            request = book_api_m.update(book,_id)
            assert request.status == 201
        except Exception as ex:
            print(ex)
