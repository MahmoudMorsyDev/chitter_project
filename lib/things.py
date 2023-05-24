# import os
# from flask import Flask, request, render_template,redirect,flash, url_for
# from lib.database_connection import get_flask_database_connection
# from lib.user import User
# from lib.users_repository import UserRepository
# from lib.message import Message
# from lib.messages_repository import MessagesRepository
# from flask_login import LoginManager, login_user, login_required, current_user, logout_user 
# import ast
# from werkzeug.security import  check_password_hash
# # Create a new Flask app

# import datetime
# current_datetime = datetime.datetime.now()
# formatted_datetime = current_datetime.strftime('%Y-%m-%d %H:%M:%S')

# app = Flask(__name__)
# app.config['SECRET_KEY'] = "Mahmoud"
# login_manager = LoginManager()
# login_manager.init_app(app)

# @login_manager.user_loader
# def load_user(user):
#     connection = get_flask_database_connection(app)
#     user_repo=UserRepository(connection)
#     user_dic = ast.literal_eval(user) 
#     return user_repo.get_user_by_id(int(user_dic['id']))

# @app.route('/home')
# def home_page():
#     connection = get_flask_database_connection(app)
#     message_repo = MessagesRepository(connection)
#     all_posts = message_repo.show_all_messages()
#     if current_user.is_authenticated:
#         return render_template('home.html',logged_in=True, all_posts = all_posts)

#     return render_template('home.html', all_posts = all_posts)


# @app.route('/home', methods=['POST'])
# def create_post():
#     connection = get_flask_database_connection(app)
#     message_repo = MessagesRepository(connection)
#     message_body =  request.form['message_body']
#     if not valid_input(message_body):
#         flash("Not a valid post")
#         return redirect('/home')
#     else:
#         new_message = Message(None, 'guest',message_body,formatted_datetime)
#         message_repo.generate_message(new_message)
#         return redirect('/home')


# @app.route('/register', methods=["GET", "POST"])
# def register_user():
#     connection = get_flask_database_connection(app)
#     user_repo=UserRepository(connection)
#     if request.method == 'POST':
#         name = request.form['your-name']
#         email = request.form['your-email']
#         user_name = request.form['your-user-name']
#         password = request.form['your-password']
#         re_password = request.form['your-repasswrod']
#         if not valid_input(name) or not valid_input(email) or not valid_input(user_name) or not valid_input(password) or not valid_input(re_password):
#             flash("Not a valid input")
#         elif exists(user_name):
#             flash("User name already taken please choose another one")
#         elif password != re_password:
#             flash("passwords do not match")
#         else:
#             new_user =User(None, name, user_name, email, password)
#             result = user_repo.register_new_user(new_user)
#             login_user(result)
#             logged_in = True
#             return redirect(url_for("home_page"))
#         return redirect('/register')
#     return render_template('register.html')



# @app.route('/login')
# def log_in_user():
#     connection = get_flask_database_connection(app)
#     user_repo=UserRepository(connection)
#     email = request.form['your-email']
#     password = request.form['your-password']
#     user = user_repo.get_user_by_email(email)
#     if not user:
#         flash("User does not exist")
#     elif not check_password_hash(user.user_password, password):
#         flash("incorrect Password")  
#     else:
#         login_user(user)   
#         logged_in = True
#         return redirect(url_for("home_page"))   
#     return render_template('login.html')




# @app.route('/logout')
# def log_out_user():
#     logout_user()
#     return redirect(url_for('home_page'))



# def valid_input(input):
#     return not input.strip() == "" or input.isspace()
# def exists(u_name):
#     connection = get_flask_database_connection(app)
#     user_repo=UserRepository(connection)
#     return user_repo.check_user_name(u_name)
# if __name__ == '__main__':
#     app.run(debug=True, port=int(os.environ.get('PORT', 5000)))
#     # if type(user_id) == str and len(user_id)>3:
#     #     print(f'id:{user_id}')
#     #     user_id = int(ast.literal_eval(user_id)['id']) 