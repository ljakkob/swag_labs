Feature: Verifiyng login funcionality
    A user can be able to log in the system with valid credentials

    @login @invalid_user
    Scenario: Log with an invalid user
        Given The user have access to the Secret Labs Page
        When The authentication is performed with login: invalidUser and password: secret_sauce
        Then The an error message is displayed: Epic sadface: Username and password do not match any user in this service

    @login @valid_user
    Scenario: Login With valid data
        Given The user have access to the Secret Labs Page
        When The authentication is performed with login: standard_user and password: secret_sauce
        Then The user can see the Products page