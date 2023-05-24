import os
from flask import Flask, request, render_template,redirect,flash, url_for
from lib.database_connection import get_flask_database_connection
from lib.user import User
from lib.users_repository import UserRepository
from lib.message import Message
from lib.messages_repository import MessagesRepository
from flask_login import LoginManager, login_user, login_required, current_user, logout_user 
import ast
from werkzeug.security import generate_password_hash, check_password_hash
# Create a new Flask app

import datetime

from lib.email import EmailSender

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY")
login_manager = LoginManager()
login_manager.init_app(app)
email = EmailSender()

@login_manager.user_loader
def load_user(user_id):
    connection = get_flask_database_connection(app)
    user_repo=UserRepository(connection)    
    return user_repo.get_user_by_id(user_id)


@app.route('/home')
def home_page():
    connection = get_flask_database_connection(app)
    message_repo = MessagesRepository(connection)
    all_posts = message_repo.show_all_messages()
    sorted_posts = sorted(all_posts, key=lambda post: post.posted, reverse=True)
    if current_user.is_authenticated:
        return render_template('home.html',current_user=current_user, all_posts = sorted_posts)

    return render_template('home.html', all_posts = sorted_posts)


@app.route('/home', methods=['POST'])
def create_post():
    current_datetime = datetime.datetime.now()
    formatted_datetime = current_datetime.strftime('%Y-%m-%d %H:%M:%S')
    connection = get_flask_database_connection(app)
    message_repo = MessagesRepository(connection)
    message_body =  request.form['message_body']
    user_repo = UserRepository(connection)
    all_users = user_repo.get_all_users()
    if not valid_input(message_body):
        flash("Not a valid post")
        return redirect('/home')
    else:
        mentioned_users = []
        mentioned_users_emails=[]
        for user in all_users:
            if f'@{user.user_name}' in message_body:
                mentioned_users.append(user.user_name)
                mentioned_users_emails.append(user.email)
        for mentioned_user in mentioned_users:
            message_body = message_body.replace(mentioned_user, f'<a href="">{mentioned_user}</a>')        
        if current_user.is_authenticated:
            new_message = Message(None, current_user.user_name,message_body,formatted_datetime,current_user.id)
            message_repo.generate_message(new_message)
            author = current_user.user_name
            if len(mentioned_users_emails) > 0:
                for mentions in mentioned_users_emails:
                    email.send_email(author, mentions)
            return redirect('/home')
        else:
            new_message = Message(None, 'guest',message_body,formatted_datetime)
            message_repo.generate_message(new_message)
            author = 'Someone'
            if len(mentioned_users_emails) > 0:
                for mentions in mentioned_users_emails:
                    email.send_email(author, mentions)
            return redirect('/home')
        


@app.route('/register', methods=["GET", "POST"])
def register_user():
    if current_user.is_authenticated:
        return redirect('/home')
    else:
        connection = get_flask_database_connection(app)
        user_repo=UserRepository(connection)
        if request.method == 'POST':
            name = request.form['your-name']
            email = request.form['your-email']
            user_name = request.form['your-user-name']
            password = request.form['your-password']
            re_password = request.form['your-repasswrod']
            if not valid_input(name) or not valid_input(email) or not valid_input(user_name) or not valid_input(password) or not valid_input(re_password):
                flash("Not a valid input")
            elif exists(user_name):
                flash("User name already taken please choose another one")
            elif password != re_password:
                flash("passwords do not match")
            else:
                hashed_pass = generate_password_hash(
                        password= password,
                        method= 'pbkdf2:sha256',
                        salt_length=8
                    )      
                new_user =User(None, name, user_name, email, hashed_pass)
                result = user_repo.register_new_user(new_user)
                login_user(result)
                # logged_in = True
                return redirect(url_for("home_page"))
            return redirect('/register')
        return render_template('register.html')



@app.route('/login', methods=["GET", "POST"])
def log_in_user():
    if current_user.is_authenticated:
        return redirect('/home')
    else:
        connection = get_flask_database_connection(app)
        user_repo=UserRepository(connection)
        if request.method == 'POST':
            email = request.form['the-email']
            password = request.form['the-password']
            the_user = user_repo.get_user_by_email(email)
            if not the_user:
                flash("User does not exist")
                return redirect('/login')
            else:
                password_valid =check_password_hash(the_user.user_password, str(password))      
                if not password_valid:
                    flash("Incorrect password")
                    return render_template('/login.html') 
                else:
                    login_user(the_user)   
                    # logged_in = True
                    return redirect(url_for("home_page"))  
        return render_template('login.html')


@app.route("/profile")
def user_profile():
    connection = get_flask_database_connection(app)
    message_repo = MessagesRepository(connection)
    if current_user.is_authenticated:

        posts = message_repo.find_messages_by_user_id(current_user.id)
        return render_template('/profile-page.html', current_user=current_user, all_posts =posts)
    else:
        return redirect('/login')

@app.route('/usersposts/<int:id>')
def find_posts(id):
    connection = get_flask_database_connection(app)
    message_repo = MessagesRepository(connection)
    posts = message_repo.find_messages_by_user_id(id)
    return render_template('/hhh.html', all_posts =posts)

@app.route('/delete/<int:id>')
def delete_post(id):
    connection = get_flask_database_connection(app)
    message_repo = MessagesRepository(connection)
    message_repo.delete_message(id)
    return redirect(request.referrer)


@app.route('/logout')
def log_out_user():
    logout_user()
    return redirect(url_for('home_page'))





def valid_input(input):
    return not input.strip() == "" or input.isspace()
def exists(u_name):
    connection = get_flask_database_connection(app)
    user_repo=UserRepository(connection)
    return user_repo.check_user_name(u_name)



if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))