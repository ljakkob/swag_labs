class CheckoutOvervivew (object):

    def __init__(self,driver):
        self.driver = driver


    def fleece_jacket_element(self):
        fleece_jacket = self.driver.find_element_by_xpath(
            "//a[@id='item_4_title_link']/parent::div//parent::div//div[@class='inventory_item_price']")
        return fleece_jacket.text

    def bike_light_element(self):
        bike_light = self.driver.find_element_by_xpath(
            "//a[@id='item_0_title_link']/parent::div//parent::div//div[@class='inventory_item_price']")
        return bike_light.text

    def element_tax(self):
        tax = self.driver.find_element_by_class_name('summary_tax_label')
        return tax.text

    def element_total (self):
       total = self.driver.find_element_by_class_name('summary_total_label')
       return total.text

    def finish(self):
        self.driver.find_element_by_class_name('cart_checkout_link').click()