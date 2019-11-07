import pytest
import requests
#fixture autouse will be used for all test before start test
@pytest.fixture(scope='session', autouse=True)
def local_cache():
    old_settings = settings.CACHES

#Also it is possible to create configuration fixture. File name conftest

#pytest --html=report.html - Console command that allow generate you report with testrun result. Available from the library "pytest-html"

@pytest.fixture()
def clear_books():
    #clear_books_id = None #wrong
    clear_books_id = []
    yield clear_books_id #for not run before test
    #if clear_books_id:
    #    requests.delete(f"{url}books/{clear_books_id}")
    for book_id in clear_books_id:
        requests.delete(f"{url}books/{book_id}")

#Don't use "id" as local variable, because many libraries already have this variable


def test_book_create(url, clear_books):
    data = {"title":"1", "author":"2"}
    r = requests.post(url+"books", data=data)
    assert r.status_code == 201
    response_body = r.json()
    #check all properites of object (verify that approach)
    for key in data:
        assert data[key] == response_body[key]
    
    get_resp = requests.get(url+"books/"+response_body['id'])
    assert get_resp.status_code == 201
    response_body = get_resp.json()
    #check all properites of object (verify that approach)
    for key in data:
        assert data[key] == response_body[key]
    #clear_books_id = post_resp_body["id"] #wrong option
    clear_books_id.append(response_body["id"]) #correct option
    # TODO: verify in get-list

@pytest.fixture()
def book_created(url):
    data = {"title":"1", "author":"2"}
    r = requests.post(url+"books", data=data)
    book = r.json()
    yield book
    if "id" in book:
        requests.delete(f"{url}books/{book_id}")
    #return book

def test_book_update(url, book_created):
    pass
#Parametrization of test

#Get params in fixture
@pytest.fixture(params=book_list, ids=[str(b) for b in book_list])
def book(requests, url):
    b = requests.param
    return b


