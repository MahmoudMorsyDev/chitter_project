from werkzeug.security import generate_password_hash
from flask_login import UserMixin

class User(UserMixin):
 
    def __init__(self, id, name, user_name, email, user_password=None):
        self.id= id
        self.name = name
        self.user_name = user_name
        self.email = email
        if user_password != None:
            self.user_password= user_password

    # failing because the __eq__ method 
    # in the User class is comparing the 
    # password hashes (user_password) of t
    # he two user objects. Since the password 
    # hashes are generated dynamically during 
    # object initialization, the hashes for user1 
    # and user2 will be different
    # , even if the passwords are the same.    
    # def __eq__(self, other):
    #     return self.__dict__ == other.__dict__

    # ---------------------------------------
    # compares only the id, user_name, and email 
    # attributes for equality, ignoring the user_password 
    # attribute. This allows the comparison to return 
    # True for two User objects with matching id, user_name,
    # and email values, regardless of their password hashes.
    def __eq__(self, other):
        if isinstance(other, User):
            return (
            self.id == other.id and
            self.name == other.name and
            self.user_name == other.user_name and
            self.email == other.email
            )
        return False
    #the __repr__ method returns a masked placeholder 
    # (<masked>) for the user_password attribute. 
    # This ensures that the password value or hash 
    # is not revealed in the string representation.
    def __repr__(self):
        return f"User({self.id}, {self.name}, {self.user_name}, {self.email}, <masked>)"
        