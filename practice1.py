import time
from selenium import webdriver

# Optional argument, if not specified will search path.
driver = webdriver.Chrome()
driver.get('http://www.google.com/xhtml');
time.sleep(5)

search_box = driver.find_element_by_name('q')
search_box.send_keys('ChromeDriver')
search_box.submit()
time.sleep(5)

driver.quit()