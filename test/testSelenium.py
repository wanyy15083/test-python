from selenium import webdriver
import time
import selenium.webdriver.chrome.service as service
from selenium.webdriver.common.keys import Keys

service = service.Service('F:/JavaSoftware/python/chromedriver.exe')
service.start()
capabilities = {'chrome.binary': 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe'}
driver = webdriver.Remote(service.service_url, capabilities)
# driver.get('http://www.baidu.com/');
# time.sleep(5) # Let the user actually see something!
# driver.quit()

driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
print driver.page_source