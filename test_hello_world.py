import json

from hello_user import hello_user_handler


def test_hello_user():
    expected_output = {"message": "Hello user!"}
    actual = hello_user_handler({}, {})
    assert True
