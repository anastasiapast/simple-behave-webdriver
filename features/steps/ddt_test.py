from behave import given, when,then
from selenium import webdriver
from selenium.webdriver.support.ui import Select

@when("I open practiceselenium website")
def step_impl(context):
    context.driver.get("http://www.practiceselenium.com/practice-form.html")

@when('I fill "{firstname}" "{lastname}" "{sex}" "{yrs}" "{date_stopped}"')
def step(context, firstname, lastname, sex, yrs, date_stopped):
    context.driver.find_element_by_name("firstname").send_keys(firstname)
    context.driver.find_element_by_name("lastname").send_keys(lastname)
    sex_element = next(element for element in context.driver.find_elements_by_name("sex") if element.get_attribute("value")==sex)
    sex_element.click()
    yrs_element = next(element for element in context.driver.find_elements_by_tag_name("input") if
                       element.get_attribute("value") == yrs)
    yrs_element.click()
    context.driver.find_element_by_id('datepicker').send_keys(date_stopped)

@when('I fill "{tea}" "{excited_about}" "{continent}" and "{selenium_commands}"')
def step(context, tea, excited_about, continent, selenium_commands):
    tea_element = next(element for element in context.driver.find_elements_by_tag_name("input") if
                       element.get_attribute("value") == tea)
    tea_element.click()
    excited_element = next(element for element in context.driver.find_elements_by_name("tool") if
                       element.get_attribute("value") == excited_about)
    excited_element.click()

    contitents_select = Select(context.driver.find_element_by_id('continents'))
    contitents_element = next(element for element in contitents_select.options if element.text==continent)
    contitents_element.click()

    another_select_list = Select(context.driver.find_element_by_id('selenium_commands'))
    another_select_list = next(element for element in another_select_list.options if element.text==selenium_commands)
    another_select_list.click()


@when('I hit submit button')
def step(context):
    context.driver.find_element_by_id('submit').click()


@then('I go back to Welcome page and verify title')
def step(context):
    title = context.driver.title
    assert 'Welcome' in title
