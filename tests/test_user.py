from werkzeug.security import  check_password_hash

from lib.user import User

def test_user_construct():
    user = User(1, 'John','john50', 'John@email.com', 'john123')
    assert user.id == 1
    assert user.name == 'John'
    assert user.user_name == 'john50'
    assert user.email == 'John@email.com'
    assert user.user_password== "john123"

def test_users_are_equal():
    user1 = User(1, 'John','john50', 'John@email.com', 'john123')
    user2 = User(1, 'John','john50', 'John@email.com', 'john123')
    assert user1 == user2
def test_user_format():
    user1 = User(1, 'John', 'john50', 'John@email.com', 'john123')
    assert str(user1)== "User(1, John, john50, John@email.com, <masked>)"


        