
DROP TABLE IF EXISTS messages;
DROP SEQUENCE IF EXISTS users_id_seq;
DROP TABLE IF EXISTS users;
DROP SEQUENCE IF EXISTS users_id_seq;


CREATE SEQUENCE IF NOT EXISTS users_id_seq;
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    user_name VARCHAR(255),
    email VARCHAR(255),
    user_password VARCHAR(255)
);

CREATE SEQUENCE IF NOT EXISTS messages_id_seq;
CREATE TABLE messages (
    id SERIAL PRIMARY KEY,
    author VARCHAR(255),
    body TEXT, 
    posted TIMESTAMP,
    user_id  Int,
    constraint fk_user foreign key(user_id) references users(id) on delete cascade 
);

INSERT INTO users (name, user_name, email, user_password) VALUES ('John','john50', 'john@mail.com', 'john123');
INSERT INTO users (name, user_name, email, user_password) VALUES ('Sam','sam50', 'sam@mail.com', 'sam123');

INSERT INTO messages (author, body, posted, user_id) VALUES ('sam50', 'this is the first test message', '2023-05-19 10:30:45', 2);
INSERT INTO messages (author, body, posted, user_id) VALUES ('john50','second test message for chitter', '2022-03-11 11:30:45', 1);