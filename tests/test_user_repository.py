from lib.user import User
from lib.users_repository import UserRepository

def test_get_all_users(db_connection):
    db_connection.seed("seeds/chitter.sql")
    repository = UserRepository(db_connection)
    all_users = repository.get_all_users()
    assert all_users == [
        User(1, 'John','john50', 'john@mail.com', '<masked>'),
        User(2,'Sam','sam50', 'sam@mail.com', '<masked>')
    ]

def test_register_new_user(db_connection):
    db_connection.seed('seeds/chitter.sql')
    repository = UserRepository(db_connection)
    new_user = User(None, "Mahmoud",'mahmoud50', 'Mahmoud@mail.com', 'Mahmoud123')
    repository.register_new_user(new_user)
    assert repository.get_all_users() ==[
        User(1, 'John','john50', 'john@mail.com', '<masked>'),
        User(2,'Sam','sam50', 'sam@mail.com', '<masked>'),
        User(3,'Mahmoud','mahmoud50', 'Mahmoud@mail.com', '<masked>')
    ]

def test_check_user_name(db_connection):
    db_connection.seed('seeds/chitter.sql')
    repository = UserRepository(db_connection)
    assert repository.check_user_name('sam50') == True
    assert repository.check_user_name('mahmoud') == False

# def test_get_user_by_email(db_connection):
#     db_connection.seed('seeds/chitter.sql')
#     repository = UserRepository(db_connection) 
#     new_user = User(None, "Mahmoud",'mahmoud50', 'Mahmoud@mail.com', 'Mahmoud123')
#     repository.register_new_user(new_user) 
#     assert repository.get_user_by_email('Mahmoud@mail.com') == [
#         User(3,'Mahmoud','mahmoud50', 'Mahmoud@mail.com', '<masked>')
#         ]
     