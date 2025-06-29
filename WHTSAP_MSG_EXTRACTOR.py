from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd
import time
import os


# https://sj9yjfy94d3g3q9g-56934695015.shopifypreview.com/
# pass: beaterr  

'''
BUGS:
Logging Out is not working properly
        Line 141 - 168
'''

'''
Features can be added:
    - How much messages user wants extract(i.e Number of Messages)
    - From which Month/Day/Year user want to extract message
    - Or Range of time period of messages have to be extracted:
        For Example: 
            - from january 1, 2024 to january 10, 2024 
            - From january 1, 2024 to febuary 1, 2024
    - If No. of messages = 0, or Showing "Syncing older messages"
        - Then handle the error, show there's no messages available
          or show Syncing older message and wait
'''




path = "D:/UniqueDressup/chromedriver-win64/chromedriver.exe"
ser = Service(executable_path=path)
driver = webdriver.Chrome(service=ser)

# Open whatsapp web
driver.get("https://web.whatsapp.com")
print("Please scan the QR code with your WhatsApp app.")
time.sleep(30)

Contact_name = "PRODUCT_INFO" # Ex(Syncing Older messages)
# Contact_name = "Manan Jain" # Ex(Messages available and extracted)
 


'''
* find_element() - returns a single web element matching the provided 
                   locator strategy.
* By.XPATH - are used to navigate through elements and attribute in 
             an XML document(or HTML structure in this case).
*'//div[@contenteditable="true"][@data-tab="3"]' 
    - //div: this selets all <div> elements anywhere in the document.
    - [@contenteditable="true"]: this is a condition to select a <div>
                                 element that has the attribute
                                 contenteditable="true".(this means
                                 the element is editable, such as a 
                                 text input field).
    - [@data-tab="3"]: this condition further refines the selection to 
                       <div> elements that also have an attribute 
                       data-tab="3".(it is specific to whatsapp web's 
                       structure, and in this case, it refers to the 
                       element containing the search box)

'''

search_box = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]')))
search_box.click()
search_box.send_keys(Contact_name)
time.sleep(10)

'''
*contact_name: variable that contains contact name or group you're trying 
              to locate.
*f'//span[@title="{contact_name}"]': XPATH query is used to find an element
                                     of type <span> with a title attribute 
                                     that matches the contact_name.
    - //span: this selects all <span> elements on the page.
    - [@title="{content_name}"]: this filters <span> elements to only those
                                 title attribute exactly matchs the value 
                                 of contact_name. The title attribute in 
                                 WhatsApp Web typically holds the name 
                                 of a contact or group.
*contact.click(): After locating the contact, the click method simulates a 
                  mouse click on the found element.(that is contact's name,
                  which opens the chat with that contact or group).
'''
contact = driver.find_element(By.XPATH, f'//span[@title="{Contact_name}"]')
contact.click()

 
messages = driver.find_elements(By.XPATH, '//div[contains(@class, "message-in") or contains(@class, "message-out")]//span[contains(@class, "selectable-text")]')
timestamps = driver.find_elements(By.XPATH, '//div[contains(@class, "message-in") or contains(@class, "message-out")]//span[contains(@class, "x1rg5ohu")]')

# Create a list to store messages and timestamps
chat_data = []

# Loop through messages and timestamps and collect the data
for message, timestamp in zip(messages, timestamps):
    chat = message.text
    time_of_msg = timestamp.text
    # print(f"{chat}")
    chat_data.append([chat])
no_of_msg = len(chat_data)


if no_of_msg == 0:
    # let the page load the messages for a few seconds
    print("Syncing Older Messages")
    # Add Waiting for Syncing Older messages
    synchronize = WebDriverWait(driver, 30).until(EC.presence_of_all_elements_located((By.XPATH, '//div[contains(@class, "message-in") or contains(@class, "message-out")]//span[contains(@class, "selectable-text")]')))
    # extract messages
    messages = driver.find_elements(By.XPATH, '//div[contains(@class, "message-in") or contains(@class, "message-out")]//span[contains(@class, "selectable-text")]')
    timestamps = driver.find_elements(By.XPATH, '//div[contains(@class, "message-in") or contains(@class, "message-out")]//span[contains(@class, "x1rg5ohu")]')
    # Create a list to store messages and timestamps
    chat_data = []

    # Loop through messages and timestamps and collect the data
    for message, timestamp in zip(messages, timestamps):
        chat = message.text
        time_of_msg = timestamp.text
        print(f"{chat}")
        chat_data.append([chat])
    no_of_msg = len(chat_data)    
    print("---------------------")
    print(f"Number of Messages extracted : {no_of_msg}")

else:
    # Create a list to store messages and timestamps
    chat_data = []

    # Loop through messages and timestamps and collect the data
    for message, timestamp in zip(messages, timestamps):
        chat = message.text
        time_of_msg = timestamp.text
        print(f"{chat}")
        chat_data.append([chat])
    no_of_msg = len(chat_data)
    print("---------------------")
    print(f"Number of Messages extracted : {no_of_msg}")

'''
# Log-out from WhatsApp Web
# Find and Click the Menu Button 
menu_btn = driver.find_element(By.XPATH, "//div[@role='button' and @title='Menu' and @aria-label='Menu']//span[@data-icon='menu']")
ActionChains(driver).move_to_element(menu_btn).click().perform()

# Wait for Menu to be fully loaded
wait = WebDriverWait(driver, 30)

# Find and Click the Log-out Button
# log_out = driver.find_element(By.XPATH, '//li[@role="button"]//div[@aria-label="Log out"]')
# log_out = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Log out']")))
log_out = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@aria-label="Log out" and text()="Log out"]')))
log_out.click()
print("Logging Out....")

# confirm the log-out
confirm = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button//div[text()='Log out']"))
)
confirm.click()
time.sleep(5)
print("You are successfully logged out.")

#close the browser window
driver.close()
print("Browser closed successfully.")
'''