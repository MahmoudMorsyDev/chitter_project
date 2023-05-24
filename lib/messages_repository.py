from lib.message import Message
import datetime
current_datetime = datetime.datetime.now()
# print(current_datetime)

class MessagesRepository:
    def __init__(self, connection):
        self._connection = connection

    def show_all_messages(self):
        rows = self._connection.execute('SELECT * from messages')
        all_messages = []
        for row in rows:
            message = Message(row['id'], row['author'], row['body'], row['posted'], row['user_id']) 
            all_messages.append(message)
            # print(row['author'])
        return all_messages
        
    def generate_message(self, new_message):
        self._connection.execute('INSERT INTO messages (author, body, posted, user_id) VALUES(%s, %s,%s,%s)', [new_message.author, new_message.body, new_message.posted, new_message.user_id])
        # print(new_message.posted)

    def delete_message(self, message_id):
        self._connection.execute(
            "DELETE from messages where id=%s",[message_id]
        )

    def find_messages_by_user_id(self, user_id):
        all_posts = self.show_all_messages()
        return [post for post in all_posts if post.user_id == user_id]        