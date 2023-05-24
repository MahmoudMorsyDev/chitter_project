from playwright.sync_api import Page, expect
from lib.user import User
from lib.users_repository import UserRepository
import time

def test_home_page(db_connection, page, test_web_address):
    db_connection.seed("seeds/chitter.sql")
    page.goto(f'http://{test_web_address}/home')
    h1_item = page.locator(".hello-guest")
    expect(h1_item).to_have_text('Hello Guest')
    posts_list = page.locator('.all_posts_list')
    expect(posts_list).to_contain_text([
        'this is the first test message',
        "second test message for chitter"
    ])

def test_add_new_post(db_connection, page, test_web_address):
    db_connection.seed("seeds/chitter.sql")
    page.goto(f'http://{test_web_address}/home')
    page.fill("textarea[name='message_body']", "test message")
    page.click('text=Create Post')
    posts_list = page.locator('.all_posts_list')
    expect(posts_list).to_contain_text([
        "test message"
    ])
def test_invalid_post(db_connection, page, test_web_address):
    db_connection.seed("seeds/chitter.sql")
    page.goto(f'http://{test_web_address}/home')
    page.fill("textarea[name='message_body']", "")
    page.click('text=Create Post')

    invalid_message = page.locator(".invalid-message")
    expect(invalid_message).to_contain_text([
        "post"
    ])

def test_reg_form_validdation(db_connection, page, test_web_address):
    db_connection.seed('seeds/chitter.sql')
    page.goto(f'http://{test_web_address}/register')
    page.fill("input[name='your-name']", "Mahmoud")
    page.fill("input[name='your-email']", "mahmoud@email.com")
    page.fill("input[name='your-user-name']", "")
    page.fill("input[name='your-password']", "4102662")
    page.fill("input[name='your-repasswrod']", "")
    page.click('text=Complete registeration')
    invalid_input = page.locator('.invalid-message')
    expect(invalid_input).to_contain_text([
        'Not a valid input'
    ])

def test_register_user(db_connection, page, test_web_address):
    db_connection.seed('seeds/chitter.sql')
    page.goto(f'http://{test_web_address}/register')
    page.fill("input[name='your-name']", "Jack")
    page.fill("input[name='your-email']", "Jack@email.com")
    page.fill("input[name='your-user-name']", "jack50")
    page.fill("input[name='your-password']", "4102662")
    page.fill("input[name='your-repasswrod']", "4102662")
    page.click('text=Complete registeration')
    h1_locator = page.locator('.welcome-name')
    expect(h1_locator).to_contain_text([
        'Welcome Back Jack'
    ])
def test_logout_login_user(db_connection, page, test_web_address):
    db_connection.seed('seeds/chitter.sql')
    page.goto(f'http://{test_web_address}/register')
    page.fill("input[name='your-name']", "adam")
    page.fill("input[name='your-email']", "adam@emmail.com")
    page.fill("input[name='your-user-name']", "adam5050")
    page.fill("input[name='your-password']", "4102662")
    page.fill("input[name='your-repasswrod']", "4102662")
    page.click('text=Complete registeration')
    page.click('text=log out')
    h1_locator = page.locator('.hello-guest')
    expect(h1_locator).to_contain_text([
        'Hello Guest'
    ])
    # page.goto(f'http://{test_web_address}/login')
    # page.fill("input[name='the-email']", "adam@emmail.com")
    # page.fill("input[name='the-password']", "4102662")
    # page.screenshot(path="screenshot1.png", full_page=True)
    # page.click('text=login')
    # page.screenshot(path="screenshot2.png", full_page=True)
    # welcome_locator = page.locator('.welcome-name')
    # expect(welcome_locator).to_contain_text([
    #     'Welcome'
    # ])

