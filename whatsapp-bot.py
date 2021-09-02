# import library
from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
# navigate to whatsapp web
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://web.whatsapp.com/')
time.sleep(30)
# define contacts and groups to send message
contacts = ['Friends'] # insert group name or contact name
message = 'Hello' # insert message
# search for contacts/group
def search_contact(contact):
    search_field = driver.find_element_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
    time.sleep(3)
    search_field.click()
    search_field.send_keys(contact)
    search_field.send_keys(Keys.ENTER)

def send_message(message):
    message_field = driver.find_elements_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
    message_field[1].click()
    time.sleep(3)
    message_field[1].send_keys(message)
    message_field[1].send_keys(Keys.ENTER)
for contact in contacts:
    search_contact(contact)
    send_message(message)

# search filed 'copyable-text selectable-text'
# search filed private ' copyable-text selectable-text'
# send messages to contact/group