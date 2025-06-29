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
FEATURES:

    - How much messages user wants extract(i.e Number of Messages)
    - From which Month/Day/Year user want to extract message
    - Or Range of time period of messages have to be extracted:
        For Example: 
            - from january 1, 2024 to january 10, 2024 
            - From january 1, 2024 to febuary 1, 2024
    - If No. of messages = 0, or Showing "Syncing older messages"
        - Then handle the error, show there's no messages available
          or show Syncing older message and wait

    - line 237: 
        return {
        "Name": name,
        "Title": name,
        "Product Category": category,
        "Tags": category,
        "Option1 Value": color,
        "Variant Grams": weight,
        "Variant Price": price,
        "Material & Care": material_care,
        "Description": description,
        "Size-Quantity": size_quantity_data
        "Size (product.metafields.shopify.size)": size(size1;size2)
        "Color (product.metafields.shopify.color-pattern)" : color (color1;color2)
    }
    
'''

'''
BUGS:
Logging Out is not working properly
        Line 141 - 168
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

# # Log-out from WhatsApp Web
# # Find and Click the Menu Button 
# menu_btn = driver.find_element(By.XPATH, "//div[@role='button' and @title='Menu' and @aria-label='Menu']//span[@data-icon='menu']")
# ActionChains(driver).move_to_element(menu_btn).click().perform()

# # Wait for Menu to be fully loaded
# wait = WebDriverWait(driver, 30)

# # Find and Click the Log-out Button
# # log_out = driver.find_element(By.XPATH, "//div[@role='button' and @aria-label='Log out' and text()='Log out']")
# # log_out = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Log out']")))
# log_out = wait.until(EC.element_to_be_clickable((By.XPATH, '//li[@role="button"]//div[@aria-label="Log out"]')))
# log_out.click()
# print("Logging Out....")

# # confirm the log-out
# confirm = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable((By.XPATH, "//button//div[text()='Log out']"))
# )
# confirm.click()
# time.sleep(5)
# print("You are successfully logged out.")

# #close the browser window
# driver.close()
# print("Browser closed successfully.")


# code to Insert data into CSV File

# Function to process input
def process_input_data(data):
    lines = data[0].strip().split('\n')
    
    # Extract relevant fields
    name = lines[0]
    category = lines[1]
    color = lines[2]
    weight = lines[3]
    price = lines[4]
    material_care = lines[5]
    description = lines[6] if len(lines) > 6 else ""  # Add description if it exists
    size_quantity = lines[7:]

    size_quantity_data = []
    metafield_color = ""
    metafield_size = ""
    
    for sq in size_quantity:
        if '-' in sq:  # Check if '-' is present
            size, quantity = sq.split('-')
            size_quantity_data.append((size.strip(), quantity.strip()))  # Strip to remove any extra whitespace
            metafield_size = ";".join([size for size, _ in size_quantity_data])
            metafield_size = metafield_size.lower()
            print(metafield_size)
        else:
            print(f"Warning: Invalid size-quantity format: {sq}")  # Handle the case where the format is not as expected

    colors = []
    for col in color:
        if ',' in col:
            color = col.split(',')
            colors.append(color)
            metafield_color = ";".join([color for color in colors])
            metafield_color = metafield_color.lower()
            print(metafield_color)
        
        else:
            metafield_color = color.lower()
            print(metafield_color)

    
    try:
        collection = {"Shirt" : "Apparel & Accessories > Clothing > Clothing Tops > Shirts",
                      "Coord Set" : "Apparel & Accessories > Clothing > Outfit Sets",
                      "Tops" : "Apparel & Accessories > Clothing > Shirts & Tops > Tops",
                      "T-Shirts" : "Apparel & Accessories > Clothing > Shirts & Tops > T-Shirts",
                      "Denim" : "Apparel & Accessories > Clothing > Pants > Jeans",
                      "Cargo" : "Apparel & Accessories > Clothing > Pants > Cargo Pants",
                      "Korean Pants" : "Apparel & Accessories > Clothing > Pants > Korean Pants",
                      "Shirts" : "Apparel & Accessories > Clothing > Shirts & Tops > Shirts",
                      "Shorts" : "Apparel & Accessories > Clothing > Shorts & Skirts",
                      "Skirts" : "Apparel & Accessories > Clothing > Shorts & Skirts",
                      "Dresses" : "Apparel & Accessories > Clothing > Dresses",
                      "Jackets" : "Apparel & Accessories > Clothing > Outerwear > Jackets",
                      "Sweatshirts" : "Apparel & Accessories > Clothing > Sweatshirts",
                      "Sweaters" : "Apparel & Accessories > Clothing > Sweaters"
        }
        if category in collection:
            category = collection[category]
            

    except Exception:
        print(f"WARNING: Category '{category}' not found in collection.")        

    
    return {
        "Name": name,
        "Title": name,
        "Product Category": category,
        "Tags": category,
        "Option1 Value": color,
        "Variant Grams": weight,
        "Variant Price": price,
        "Material & Care": material_care,
        "Description": description,
        "Size-Quantity": size_quantity_data,
        "Size (product.metafields.shopify.size)": metafield_size,
        "Color (product.metafields.shopify.color-pattern)" : metafield_color
    }

# Process the input data
for i in range(len(chat_data)):
    input_data = chat_data[i]
    print(f'Inserting Data {chat_data[i][0]}:\n {chat_data[i]}\n') 
    product_data = process_input_data(input_data)
    print(product_data)

    # Create a DataFrame from the processed product data
    size_quantity_data = product_data['Size-Quantity']
    new_df = pd.DataFrame(size_quantity_data, columns=['Size', 'Quantity'])

    # Add product information only in the first row
    new_df['Title'] = product_data['Title']
    new_df['Product Category'] = product_data['Product Category']
    new_df['Tags'] = product_data['Tags']
    new_df['Option1 Value'] = product_data['Option1 Value']
    new_df['Variant Grams'] = float(product_data['Variant Grams'])  # Convert to float
    new_df['Variant Price'] = float(product_data['Variant Price'])  # Convert to float
    new_df['Material & Care'] = product_data['Material & Care']
    new_df['Description'] = product_data['Description']  # Add Description column
    new_df['Size (product.metafields.shopify.size)'] = product_data['Size (product.metafields.shopify.size)']
    new_df['Color (product.metafields.shopify.color-pattern)'] = product_data['Color (product.metafields.shopify.color-pattern)']

    # Insert size and quantity values directly into Option2 Value and Variant Inventory Qty columns
    new_df['Option2 Value'] = new_df['Size']
    new_df['Variant Inventory Qty'] = new_df['Quantity']

    # Rearrange columns to have product info at the beginning
    new_df = new_df[['Title', 'Product Category', 'Tags', 'Option1 Value', 'Variant Grams', 'Variant Price', 'Material & Care', 'Description', 'Color (product.metafields.shopify.color-pattern)', 'Size (product.metafields.shopify.size)', 'Option2 Value', 'Variant Inventory Qty']]

    # Ensure only the first row has product information
    new_df.loc[1:, ['Title', 'Product Category', 'Tags', 'Option1 Value', 'Variant Grams', 'Variant Price', 'Material & Care', 'Description', 'Color (product.metafields.shopify.color-pattern)', 'Size (product.metafields.shopify.size)']] = None

    # Define the CSV file name
    # file_name = "client_product_data.csv"
    file_name = "TrashData.csv"

    # Check if the file exists
    if os.path.exists(file_name):
        # Load existing data
        existing_df = pd.read_csv(file_name)

        # Check for relevant columns
        for column in ['Title', 'Product Category', 'Tags', 'Option1 Value', 'Variant Grams', 'Variant Price', 'Material & Care', 'Description', 'Color (product.metafields.shopify.color-pattern)', 'Size (product.metafields.shopify.size)', 'Option2 Value', 'Variant Inventory Qty']:
            if column not in existing_df.columns:
                print(f"Warning: Column '{column}' not found in existing CSV. It will be ignored.")

        # Insert new data into specific columns of the existing DataFrame
        combined_df = existing_df.copy()

        # Concatenate the new data to the combined DataFrame
        combined_df = pd.concat([combined_df, new_df], ignore_index=True)

        # Forward fill the columns where necessary
        # combined_df[['Title', 'Product Category', 'Option1 Value', 'Material & Care']] = combined_df[['Title', 'Product Category', 'Option1 Value', 'Material & Care']].ffill()

    else:
        # If the file does not exist, use the new DataFrame as the combined DataFrame
        combined_df = new_df

    # Save the combined DataFrame back to the CSV file
    combined_df.to_csv(file_name, index=False)

print("Data successfully appended to 'TrashData.csv'.")
