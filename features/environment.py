from selenium import webdriver
import os

def before_all(context):
    context.driver = webdriver.Chrome("C:/seleniumDrivers/chromedriver.exe")

# def after_scenario(context, scenario):
#     print("scenario status " + scenario.status)
#     if scenario.status == "failed":
#         if not os.path.exists("failed_scenarious_screenshots"):
#             os.makedirs("failed_scenarious_screenshots")
#         os.chdir("failed_scenarious_screenshots")
#         context.driver.save_screenshot(scenario.name + "_failed.png")

def after_all(context):
    context.driver.quit()