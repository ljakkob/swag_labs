class Checkout(object):

    def __init__(self, driver):
        self.driver = driver

    def name_checkout(self, name):
        self.driver.find_element_by_css_selector("input[placeholder='First Name']").send_keys(name)

    def last_name_checkout(self, last_name):
        self.driver.find_element_by_css_selector("input[placeholder='Last Name']").send_keys(last_name)

    def zip_code(self, zip_code):
        self.driver.find_element_by_css_selector("input[placeholder='Zip/Postal Code']").send_keys(zip_code)

    def submit(self):
        self.driver.find_element_by_css_selector("input[type='submit']").click()