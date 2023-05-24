class Message:
    def __init__(self,id, author, body, posted, user_id=None, ):
        self.id = id
        self.author = author
        self.body = body
        self.posted = posted
        self.user_id = user_id

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    def __repr__(self):
        return f"Message({self.id}, {self.author}, {self.body}, {self.posted}, {self.user_id})"