class CheckoutComplete(object):

    def __init__(self, driver):
        self.driver = driver

    def order_complete_element(self):
        order_complete = self.driver.find_element_by_class_name('complete-header')
        return order_complete.text