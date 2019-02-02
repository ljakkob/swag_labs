from behave import *
from Pages.InventoryPage import Inventory
from Pages.CartPage import Cart
from Pages.CheckoutPage import Checkout
from Pages.CheckoutOverviewPage import CheckoutOvervivew
from Pages.CheckoutCompletePage import CheckoutComplete
import  time


@given('The user add this itens to the cart: {item1}, {item2} and {item3}')
def step_impl(context, item1, item2, item3):
    iventory = Inventory(context.driver)
    iventory.btn_item(item1)
    iventory.btn_item(item2)
    iventory.btn_item(item3)
    iventory.cart()

@given('Remove {item} of the cart')
def step_impl(context, item):
    cart = Cart(context.driver)
    cart.remove_item(item)
    cart.checkout()
    time.sleep(5)

@when('The checkout information is filled with name {name} {last_name} and zipcode {zipcode}')
def step_impl(context, name, last_name,zipcode):
    checkout = Checkout(context.driver)
    checkout.name_checkout(name)
    checkout.last_name_checkout(last_name)
    checkout.zip_code(zipcode)
    checkout.submit()

@then(u'The purchase is finished')
def step_impl(context):

    def element_to_float(element):
        float_price = element.replace('$', '').replace('Tax:', '').replace('Total:', '')
        float_price = float(float_price)
        return float_price

    checkout_overview = CheckoutOvervivew(context.driver)
    bike_light = checkout_overview.bike_light_element()
    fleet_jacket = checkout_overview.fleece_jacket_element()
    tax_element = checkout_overview.element_tax()
    total_element = checkout_overview.element_total()

    bike_light_price = element_to_float(bike_light)
    fleet_jacket_price = element_to_float(fleet_jacket)
    tax_value = element_to_float(tax_element)
    total_value = element_to_float(total_element)

    total_order = bike_light_price + fleet_jacket_price+ tax_value
    assert total_order == total_value

    checkout_overview.finish()

@then('The message {order_complete} is displayed')
def step_impl(context, order_complete):
    checkout_complete = CheckoutComplete(context.driver)
    order_complete_message = checkout_complete.order_complete_element()

    assert order_complete == order_complete_message