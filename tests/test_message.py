from lib.message import Message

def test_message_construct():
    message = Message(1, 'sam50', 'this is a test message', "2023-05-19 10:30:45", 1)
    assert message.id == 1
    assert message.author == 'sam50'
    assert message.body == 'this is a test message'
    assert message.posted == "2023-05-19 10:30:45"
    assert message.user_id ==1

def test_messages_are_equal():
    message_1= Message(1,'sam50', 'this is a test message', "2023-05-19 10:30:45", 1)
    message_2= Message(1, 'sam50','this is a test message', "2023-05-19 10:30:45", 1)  
    assert message_1 == message_2    

def test_message_format():
    message_1= Message(1, 'sam50', 'this is a test message', "2023-05-19 10:30:45", 1)
    assert str(message_1) == 'Message(1, sam50, this is a test message, 2023-05-19 10:30:45, 1)'