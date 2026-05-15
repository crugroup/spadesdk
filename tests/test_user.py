from spadesdk.user import User


def test_user_instantiation():
    user = User(id=1, email="a@b.com", first_name="Alice", last_name="Smith")
    assert user.id == 1
    assert user.email == "a@b.com"
    assert user.first_name == "Alice"
    assert user.last_name == "Smith"
