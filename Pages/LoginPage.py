

class Login(object):

        def __init__(self, driver):
            self.driver = driver

        def UserName(self, username):
            self.driver.find_element_by_id('user-name').send_keys(username)

        def Password(self, password):
            self.driver.find_element_by_id('password').send_keys(password)

        def LoginButton(self):
            self.driver.find_element_by_class_name('login-button').click()

        def Error_Message(self):
            error_message_element = self.driver.find_element_by_css_selector('h3[data-test]')
            error_message_element = error_message_element.text
            return error_message_element