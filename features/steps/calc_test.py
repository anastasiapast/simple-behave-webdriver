from behave import given, when,then

@given("I have two integers a and b")
def step(context):
    context.a = 1
    context.b = 1

@when("I add the numbers")
def step(context):
    context.sum = int(context.a) + int(context.b)

@then("I print the addition result")
def step(context):
    print(f"Sum = {context.sum}")
    assert context.sum == 2


@then("The result is correct")
def step(context):
    assert context.sum == 2