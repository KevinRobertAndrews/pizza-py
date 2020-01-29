# USE PYTHON AND SELENIUM TO ORDER A PIZZA.PY
# This script orders pizza from Season's Pizza.
# It does so by navagating through Season's website, like a real user.

# THE ORDER >>
# Two large pizzas, both with bacon, chicken, and hot peppers.
# Four garlic bread
# Four garlic sauce
# Two diet cokes


# ---------------------------------------------------------------------


from selenium import webdriver
import time


# Wrapper for calls to get id
def clickId(id):
    return browser.find_element_by_id(id).click()


# We will need to pause every so often to make sure that
# the webpage is able to fully load.
def sleep():
    time.sleep(2)


# ---------------------------------------------------------------------


# Initialize browser
browser = webdriver.Chrome("C:\\Users\\Kevin\\chromedriver.exe")

# Browse to Seasons Pizza and click on the delivery button
browser.get('https://seasonspizzaottawa.ca/')
clickId('img_delivery')

sleep()

# Choose the right pizza deal
clickId("m_21107")

sleep()

# Make it large
clickId("extra_35250_1")
clickId("nextStep_extras_1_0")

# First pizza toppings
clickId("ci_9475_2")  # Topping
clickId("ci_9475_2-2")  # Whole pizza
clickId("ci_9479_2")
clickId("ci_9479_2-2")
clickId("ci_9470_2")
clickId("ci_9470_2-2")
clickId("nextStep_custom_ingredients_2_1")

# Second pizza toppings
clickId("ci_9475_3")
clickId("ci_9475_3-2")
clickId("ci_9479_3")
clickId("ci_9479_3-2")
clickId("ci_9470_3")
clickId("ci_9470_3-2")
clickId("nextStep_custom_ingredients_3_1")

# Skip additional toppings
clickId("nextStep_custom_ingredients_4_2")
clickId("nextStep_custom_ingredients_5_3")

# Add four garlic sauce
clickId("sauces_9608_6")
clickId("sauces_9608_6")
clickId("sauces_9608_6")
clickId("sauces_9608_6")
clickId("nextStep_sauces_6_4")

# Get two diet cokes
clickId("drink_9612_6")
clickId("drink_9612_6")
clickId("nextStep_drinks_6_4")

# Add to cart
clickId("placeOrderButton")

sleep()

# Place order
clickId("postOrderToCheckout")
