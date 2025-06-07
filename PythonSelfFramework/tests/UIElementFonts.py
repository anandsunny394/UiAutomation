from selenium import webdriver
from selenium.webdriver.common.by import By

# Set up the driver (Chrome in this case)
driver = webdriver.Chrome()
driver.get("https://www.google.com/") # replace with your target URL

# Find the element
element = driver.find_element(By.XPATH, "//img[@alt='Google']")

# Get the CSS properties
color = element.value_of_css_property("color")
font_size = element.value_of_css_property("font-size")


# Print the values
print("Color:", color) # e.g., 'rgba(255, 0, 0, 1)' for red
print("Font size:", font_size) # e.g., '18px'

# Verifying values (simple assertion)

assert color == "rgba(31, 31, 31, 1)"
assert font_size == "14px"



driver.quit()
