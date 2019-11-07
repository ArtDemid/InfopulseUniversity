import pytest
import api_manager
import books
import roles

@pytest.fixture()
def book():
    book = books.Book()
    return book

@pytest.fixture()
def role():
    role = roles.Role()
    return role

@pytest.fixture()
def book_api_manager(book):
    book_api_m = api_manager.ApiManager(book.base_url)
    return book_api_m

@pytest.fixture()
def role_api_manager(role):
    role_api_m = api_manager.ApiManager(role.base_url)
    return role_api_m

@pytest.fixture()
def role_test_data(role):
    data = role.load_test_data()
    return data

@pytest.fixture()
def book_test_data(book):
    data = book.load_test_data()
    return data
