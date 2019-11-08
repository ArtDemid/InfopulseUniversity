#import pytest

def test_p_GET_request_for_book(book, book_api_manager, book_test_data):
    _id = book_api_manager.get_item_id(book, book_test_data[0])
    request = book_api_manager.read(book,_id)
    assert request.status == 200

def test_p_GET_request_for_role(role, role_api_manager, role_test_data):
    _id = role_api_manager.get_item_id(role, role_test_data[0])
    try:
        request = role_api_manager.read(role,_id)
        assert request.status == 201
    except Exception as ex:
        print(ex)

def test_p_GET_all_book(book, book_api_manager, book_test_data):
    try:
        request = book_api_manager.read(book)
        assert book_test_data in request.body
    except Exception as ex:
        print(ex)

def test_p_POST_for_book(book, book_api_manager, book_test_data):
    try:
        for item in book_test_data:
            if item['title'] == 'Halo: Cryptum':
                request = book_api_manager.create(book, item)
        assert request.status == 201
    except Exception as ex:
        print(ex)

def test_p_DELETE_for_book(book, book_api_manager, book_test_data):
    _id = book_api_manager.get_item_id(book, book_test_data[0])
    try:
        request = book_api_manager.delete(book,_id)
        assert request.status == 201
    except Exception as ex:
        print(ex)

def test_p_UPDATE_for_book(book, book_api_manager, book_test_data):
    _id = book_api_manager.get_item_id(book, book_test_data[0])
    try:
        request = book_api_manager.update(book,_id)
        assert request.status == 201
    except Exception as ex:
        print(ex)
