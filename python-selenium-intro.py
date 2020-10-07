import time
from selenium import webdriver

driver = webdriver.Chrome('/path/to/chromedriver')  # Optional argument, if not specified will search path.
driver.get('http://www.google.com/'); # Fetch required url
time.sleep(5) # Let the user actually see something!
search_box = driver.find_element_by_name('q') # Get the search box
search_box.send_keys('ChromeDriver') # Input text
search_box.submit() # Press submit button
time.sleep(5) # Let the user actually see something!
driver.quit()
