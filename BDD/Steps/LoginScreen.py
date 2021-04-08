from behave import given, then, when


@given(u'Launch the app and click on login button')
def methodOne(context):
    print("L1 - Launching the app")


@when(u'Enter UserID')
def methodTwo(context):
    print("L2 - Enter the user ID in the Login Screen")


@when(u'Enter Password')
def methodThree(context):
    print("L3 - Enter the password in the Login Screen")


@when(u'Click on Login Button')
def methodFour(context):
    print("L4 - CLick on to the Login Button")


@when(u'Home Page Opens')
def mehodFive(context):
    print("L5 - Home page opened")


@then(u'Verify Home Screen')
def methodSix(context):
    print("L6 - Home screen opened")