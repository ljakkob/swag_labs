Feature: Order product
  A user can be able to access the page, add products to the cart and finish the purchase

  Background: The user is authenticaded
    Given The user have access to the Secret Labs Page
    When The authentication is performed with login: standard_user and password: secret_sauce
    Then The user can see the Products page

  @order_product
  Scenario: Purchase item
      Given The user add this itens to the cart: Sauce Labs Backpack, Sauce Labs Bike Light and Sauce Labs Fleece Jacket
      And  Remove Sauce Labs Fleece Jacket of the cart
      When The checkout information is filled with name New Tester and zipcode 41610-660
      Then The purchase is finished
      And  The message THANK YOU FOR YOUR ORDER is displayed
