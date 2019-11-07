import requests
import json


# @pytest.mark.parametrize("data", books_list, ids=[str(b) for b in books_list])
def test_book_create(app, book, clear_books):
    res = app.create(book)
    print(res.reason)
    assert res.status == 201
    for key in book.to_dict():
        assert book.to_dict()[key] == res.body[key]
    # get_resp = requests.get(f"{url}books/{post_resp_body['id']}")
    # assert get_resp.status_code == 200
    # get_resp_body = get_resp.json()
    # for key in book:
    #     assert book[key] == get_resp_body[key]
    # book["id"] = post_resp_body["id"]
    # TODO: verify in get-list



# def test_book_update(url, book_created):
#     pass
#
#
#
# def test_role(url, book, clear_roles_by_id):
#     role = {"name": "1", "type": "2", "book": f"{url}books/{book['id']}"}
#     r = requests.post(url+"roles", data = role)
#     assert r.status_code == 201
#     response_data = r.json()
#     clear_roles_by_id.append(response_data["id"])
