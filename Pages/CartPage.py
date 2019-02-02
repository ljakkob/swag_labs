class Cart(object):


    def __init__(self, driver):
        self.driver = driver

    def remove_item(self,item):
        self.driver.find_element_by_xpath("//div[@class='inventory_item_name' and text()='"+ item + "']/parent::a/parent::div/parent::div//div[@class='item_pricebar']/button").click()

    def checkout(self):
        self.driver.find_element_by_link_text('CHECKOUT').click()