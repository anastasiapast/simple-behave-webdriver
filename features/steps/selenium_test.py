from behave import given, when,then
from selenium import webdriver

@given("I open {url} website")
def step(context, url):
    context.driver.maximize_window()
    context.driver.get(f"http://{url}.com")

@then('I print the title')
def step_impl(context):
   title = context.browser.title
   assert "Selenium" in title

@then("I print current url")
def step_impl(context):
    print(context.browser.current_url)

@then("I click ABOUT link")
def step_impl(context):
    context.browser.find_element_by_link_text("ABOUT").click()
    assert "ABOUT" in context.browser.title

@then("I click back on the browser")
def step_impl(context):
    context.browser.back()
    assert "Selenium" in context.browser.title

@then("I click forward on the browser")
def step_impl(context):
    context.browser.forward()
    assert "ABOUT" in context.browser.title

@then("I click refresh on the browser")
def step_impl(context):
    context.browser.refresh()

@then("print the name")
def step_impl(context):
    print(context.browser.name)
#
#
#
