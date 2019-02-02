class Inventory(object):


    def __init__(self, driver):
        self.driver = driver

    def products(self):
        products = self.driver.find_element_by_class_name('product_label')
        products = products.text
        return products

    def btn_item(self, item):
        btn_item = self.driver.find_element_by_xpath("//div[@class='inventory_item_name' and text()='"+item+"']/parent::a/parent::div/parent::div//div[@class='pricebar']/button")
        btn_item.click()

    def cart(self):
        self.driver.find_element_by_css_selector("a[href='./cart.html']").click()