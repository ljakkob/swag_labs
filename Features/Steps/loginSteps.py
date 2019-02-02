from behave import *
from selenium import webdriver
from Pages.LoginPage import Login
from Pages.InventoryPage import Inventory


@given('The user have access to the Secret Labs Page')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get('https://www.saucedemo.com')

@when('The authentication is performed with login: {username} and password: {password}')
def step_impl(context, username,password):
    login= Login(context.driver)
    login.UserName(username)
    login.Password(password)
    login.LoginButton()


@then(u'The user can see the Products page')
def step_impl(context):
    iventory = Inventory(context.driver)
    iventory_text = iventory.products()
    assert iventory_text == 'Products'

@then('The an error message is displayed: {expected_error_message}')
def step_impl(context,expected_error_message):
    login = Login(context.driver)
    actual_error_message =login.Error_Message()
    assert  actual_error_message == expected_error_message



