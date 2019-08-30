from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time

@given("website {url}")
def step(context, url):
    context.driver.maximize_window()
    context.driver.get(f"http://{url}")

@when("push button with text '{text}'")
def step(context, text):
    WebDriverWait(context.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button")))
    context.driver.find_element_by_xpath("//button").click()

@then("page include text '{text}'")
def step(context, text):
    WebDriverWait(context.driver, 10).until(EC.presence_of_element_located
                                        ((By.XPATH, f'//*[contains(text(), "{text}")]')))
    assert context.driver.find_element_by_xpath(f'//*[contains(text(), "{text}")]')
    context.driver.quit()


