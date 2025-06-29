from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd
import time
import os

# Function to initialize the WebDriver
def init_driver(path):
    ser = Service(executable_path=path)
    driver = webdriver.Chrome(service=ser)
    return driver

# Function to log in to WhatsApp Web
def login_whatsapp(driver):
    driver.get("https://web.whatsapp.com")
    print("Please scan the QR code with your WhatsApp app.")
    time.sleep(20)

# Function to search and select a contact
def select_contact(driver, contact_name):
    search_box = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]')))
    search_box.click()
    search_box.send_keys(contact_name)
    time.sleep(10)
    contact = driver.find_element(By.XPATH, f'//span[@title="{contact_name}"]')
    contact.click()

# Function to extract messages and timestamps
def extract_messages(driver):
    messages = driver.find_elements(By.XPATH, '//div[contains(@class, "message-in") or contains(@class, "message-out")]//span[contains(@class, "selectable-text")]')
    timestamps = driver.find_elements(By.XPATH, '//div[contains(@class, "message-in") or contains(@class, "message-out")]//span[contains(@class, "x1rg5ohu")]')
    chat_data = [[message.text] for message, timestamp in zip(messages, timestamps)]
    return chat_data

# Function to log out from WhatsApp Web
def logout_whatsapp(driver):
    menu_btn = driver.find_element(By.XPATH, "//div[@role='button' and @title='Menu' and @aria-label='Menu']//span[@data-icon='menu']")
    ActionChains(driver).move_to_element(menu_btn).click().perform()
    wait = WebDriverWait(driver, 30)
    log_out = wait.until(EC.element_to_be_clickable((By.XPATH, '//li[@role="button"]//div[@aria-label="Log out"]')))
    log_out.click()
    confirm = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button//div[text()='Log out']")))
    confirm.click()
    time.sleep(5)
    driver.close()
    print("You are successfully logged out and the browser is closed.")

def process_input_data(data_string):
    lines = data_string.strip().split('\n')
    data = {
        "Name": lines[0] if len(lines) > 0 else "",
        "Category": lines[1] if len(lines) > 1 else "",
        "Color": lines[2] if len(lines) > 2 else "",
        "Weight": lines[3] if len(lines) > 3 else "",
        "Price": lines[4] if len(lines) > 4 else "",
        "Material & Care": lines[5] if len(lines) > 5 else "",
        "Description": lines[6] if len(lines) > 6 else "",
        "Size-Quantity": lines[8:] if len(lines) > 8 else []
    }
    return data

# Function to store product data in a CSV file
def store_product_data(file_name, chat_data):
    if os.path.exists(file_name):
        df = pd.read_csv(file_name)
    else:
        df = pd.DataFrame()

    for data in chat_data:
        product_data = process_input_data("\n".join(data))
        size_quantity_rows = []
        for i, size_quantity in enumerate(product_data["Size-Quantity"]):
            size, quantity = size_quantity.split("-")
            row_data = {
                "Name": product_data["Name"] if i == 0 else "",
                "Category": product_data["Category"] if i == 0 else "",
                "Color": product_data["Color"] if i == 0 else "",
                "Material & Care": product_data["Material & Care"] if i == 0 else "",
                "Description": product_data["Description"] if i == 0 else "",
                "Size": size,
                "Quantity": int(quantity)
            }
            size_quantity_rows.append(row_data)
        df_product_rows = pd.DataFrame(size_quantity_rows)
        df = pd.concat([df, df_product_rows], ignore_index=True)

    df.to_csv(file_name, index=False, na_rep="")
    print(f"Data successfully saved to {file_name}")

# Main function to run the script
def main():
    path = "D:/UniqueDressup/chromedriver-win64/chromedriver.exe"
    driver = init_driver(path)
    login_whatsapp(driver)
    contact_name = "PROD_DATA"
    select_contact(driver, contact_name)
    chat_data = extract_messages(driver)
    if not chat_data:
        print("Syncing Older Messages")
        WebDriverWait(driver, 30).until(EC.presence_of_all_elements_located((By.XPATH, '//div[contains(@class, "message-in") or contains(@class, "message-out")]//span[contains(@class, "selectable-text")]')))
        chat_data = extract_messages(driver)
    print(f"Number of Messages extracted: {len(chat_data)}")
    logout_whatsapp(driver)
    store_product_data("TrashData.csv", chat_data)

if __name__ == "__main__":
    main()