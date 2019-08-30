from behave import given, when, then
from behave import use_step_matcher
import json
from selenium.webdriver.support.ui import Select

use_step_matcher("re")

@when("I create a json string")
def step(context):
    context.json_string = '{"desc":{"someKey":"someValue","anotherKey":"value"},"main_item":{"stats":{"a":8,"b":12,"c":10}}}'

@then("I parse the string and print keys and values")
def step(context):
    json_dict = json.loads(context.json_string)
    print("Printing the json")
    print("Printing the keys and values")
    for i in json_dict:
        print(i, json_dict[i])
    print("Accessing some values...")
    print(json_dict["desc"]["someKey"])
    print(json_dict["main_item"]["stats"]["a"], "\n")

@when("I create another json string")
def step(context):
    context.another_json = json.loads('{"menu": {"id": "file","value": "File","popup": {"menuitem": ['
                                      '{"value": "New", "onclick": "CreateNewDoc()"},'
                                      '{"value": "Open", "onclick": "OpenDoc()"},'
                                      '{"value": "Close", "onclick": "CloseDoc()"}]}}}')

@then("I parse the string and print its data")
def step(context):
    print(context.another_json)
    for i in context.another_json:
        print(i, context.another_json[i])
        print("Accessiing menitem array...")
        print(context.another_json["menu"]["popup"]["menuitem"])
        print("Printing menitem array elements...")
        temp_array = context.another_json["menu"]["popup"]["menuitem"]
        for j in temp_array:
            print(j)
        print("Accessing a menuitem element as json..")
        print(temp_array[0]["value"])

@then("I persist it to a file")
def step(context):
    with open('./features/data/random.json', 'w') as outfile:
        json.dump(context.another_json, outfile)

@when("I read json string from a file")
def step(context):
    context.json_string = json.loads(open("./features/data/practiceform.json").read())

@then("I print the file contents")
def step(context):
    print(context.json_string)

@when("I read the json data file \"practiceform.json\"")
def step(context):
    context.practice_dict = json.loads(open("./features/data/practiceform.json").read())

@then("I fill the form with data from json and submit")
def step(context):
    array_rows = context.practice_dict["table"]
    for row in array_rows:
        current_row = row
        context.driver.find_element_by_name("firstname").send_keys(current_row['firstname'])
        context.driver.find_element_by_name("lastname").send_keys(current_row['lastname'])
        context.driver.find_element_by_id('sex-1').click()
        context.driver.find_element_by_id('datepicker').send_keys(current_row["date_stopped"])
        context.driver.find_element_by_id('tea2').click()
        context.driver.find_element_by_id('tool-1').click()
        continents_select = Select(context.driver.find_element_by_id('continents'))
        continents_select.options[0].click()
        another_select_list = Select(context.driver.find_element_by_id('selenium_commands'))
        another_select_list.options[0].click()
