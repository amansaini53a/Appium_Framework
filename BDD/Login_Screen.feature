# THis is feature file.

Feature: Verify the Home Screen Data
    Scenario: User Login Credentials

        Given Launch the app and click on login button
        When Enter UserID
        When Enter Password
        When Click on Login Button
        And Home Page Opens
        Then Verify Home Screen
        Then Take Screen Shot

    Scenario: Enter the data in contact form
        Given Launch the app and click on ContactUsForm
        When Enter Name
        When Enter Email
        When Enter MobileNumber
        And We need to click on submit button
        Then Click on submit button
        Then Take screenshot on contact form

