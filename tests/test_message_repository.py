from lib.message import Message
from lib.messages_repository import MessagesRepository
from datetime import datetime


def test_show_all_messages(db_connection):
    db_connection.seed('seeds/chitter.sql')
    repository = MessagesRepository(db_connection)
    all_messages = repository.show_all_messages()
    
    assert all_messages == [
        Message(1, "sam50", 'this is the first test message', datetime(2023, 5, 19, 10, 30, 45), 2),
        Message(2, "john50", 'second test message for chitter', datetime(2022, 3, 11, 11, 30, 45), 1)
    ]

def test_generate_message(db_connection):
    db_connection.seed('seeds/chitter.sql')
    repository = MessagesRepository(db_connection)
    new_message = Message(None, 'john50', "Super new message", datetime(2021, 2, 11, 11, 30, 45))
    repository.generate_message(new_message)
    # print(new_message.posted)
    assert repository.show_all_messages() == [
        Message(1, 'sam50','this is the first test message', datetime(2023, 5, 19, 10, 30, 45), 2),
        Message(2, 'john50','second test message for chitter', datetime(2022, 3, 11, 11, 30, 45), 1),
        Message(3, 'john50',"Super new message", datetime(2021, 2, 11, 11, 30, 45))
    ]

def test_delete_message(db_connection):
    db_connection.seed('seeds/chitter.sql')
    repository = MessagesRepository(db_connection)
    repository.delete_message(2)
    assert repository.show_all_messages()==([
        Message(1,'sam50', 'this is the first test message', datetime(2023, 5, 19, 10, 30, 45), 2)
    ])

def test_find_messages_by_user_id(db_connection):
    db_connection.seed('seeds/chitter.sql')
    repository = MessagesRepository(db_connection)
    assert repository.find_messages_by_user_id(1) == ([
          Message(1,'sam50', 'this is the first test message', datetime(2023, 5, 19, 10, 30, 45), 2)
    ])
