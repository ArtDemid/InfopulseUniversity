import pytest
import  requests
from models import PulseTestAPI, Book

@pytest.fixture(scope="session")
def app():
    a = PulseTestAPI("pulse-rest-testing.herokuapp.com")
    return a


books_list = [
            {"title": {"power": "Some"}, "author": "I"},
            {"title": "#$$%^&*(*()", "author": "I"},
            {"title": "рпмроиоли", "author": "I"}
        ]


@pytest.fixture(params=books_list, ids=[str(b) for b in books_list])
def book(request):
    b = Book(**request.param)
    return b
    # requests.delete(f"{url}books/{b['id']}")


@pytest.fixture()
def clear_books(app, book):
    yield
    app.delete(book)

# @pytest.fixture()
# def book_created(url):
#     r = requests.post(url + "books", data={"title": "1", "author": "2"})
#     b = r.json()
#     yield b
#     requests.delete(f"{url}books/{b['id']}")




@pytest.fixture(scope="session")
def clear_roles_by_id(url):
    id_list = []
    yield id_list
    for role_id in id_list:
        requests.delete(f"{url}roles/{role_id}")