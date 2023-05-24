from lib.user import User

class UserRepository:
    def __init__(self, connection):
        self._connection = connection

    def get_all_users(self):
        rows = self._connection.execute('SELECT * from users')
        users = []
        for row in rows:
            user = User(row['id'],row['name'], row['user_name'],row['email'], '<masked>' )
            users.append(user)
        return users        
    
    def get_user_by_email(self, email):
        rows = self._connection.execute("SELECT * from users where users.email = %s ",[email])
        # print(rows)
        if not rows:
            return False
        else:
            row = rows[0]
            return User(row['id'], row['name'], row['user_name'], row['email'], row['user_password'])
    
    def register_new_user(self, new_user):
        result = self._connection.execute("INSERT INTO users(name, user_name, email, user_password) VALUES (%s, %s, %s, %s) RETURNING id",[new_user.name, new_user.user_name, new_user.email, new_user.user_password])
        user_id = result[0]
        new_user.id = user_id
        return self.get_user_by_email(new_user.email)

    def get_user_by_id(self, user_id):
        rows = self._connection.execute("SELECT * from users where users.id = %s",[user_id])
        row = rows[0]
        return User(row['id'],row['name'], row['user_name'], row['email'], '<masked>')
    


    def check_user_name(self, user_name):
        rows = self._connection.execute("SELECT * from users where users.user_name = %s",[user_name])
        if rows:
            return True
        else:
            return False
            