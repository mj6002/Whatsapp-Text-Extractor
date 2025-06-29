from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
# driver_path = "D:/UniqueDressup/chromedriver-win64/chromedriver.exe"

class Driver:
    def __init__(self, driver_path):


    # def driver_(self, driver_path) -> str:
        self.driver_path = driver_path
        self.services = Service(executable_path=self.driver_path)
        self.driver_ = webdriver.Chrome(service=self.services) 
        self.driver_.get("https://web.whatsapp.com")
        print("Please scan the QR code with your WhatsApp app")
        time.sleep(25)

        # return self.driver_path

    def browser_exit(self):
         self.driver_.close()

class Contact(Driver):
        def __init__(self, contact_name, driver_path=None):
            Driver.__init__(self, driver_path)
            self.contact_name = contact_name
            self.driver_path = driver_path

        def find_Contact(self):
            self.search_box = self.driver_.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]')
            self.search_box.click()
            self.search_box.send_keys(self.contact_name)
            time.sleep(10)
            self.contact = self.driver_.find_element(By.XPATH, f'//span[@title="{self.contact_name}"]')
            self.contact.click()
            time.sleep(15)

class ChatText(Driver):
    def __init__(self, messages, driver_path, driver_):
         self.messages = messages
         Driver().__init__(self, driver_path, driver_)

         
    def extract_messages(self):
        self.messages = self.driver_.find_elements(By.XPATH, '//div[contains(@class, "message-in") or contains(@class, "message-out")]//span[contains(@class, "selectable-text")]')
        self.timestamps = self.driver_.find_elements(By.XPATH, '//div[contains(@class, "message-in") or contains(@class, "message-out")]//span[contains(@class, "x1rg5ohu")]')

        # Store message and timestamps in a list
        self.chat_data = []

        for self.message, self.timestamp in zip(self.messages, self.timestamps):
            self.chat = self.message.text
            self.time_of_msg = self.timestamp.text
            print(f"[{self.chat}")
            self.chat_data.append([self.chat])
        self.no_of_msg = len(self.chat_data)
        print("--------------------------")
        print(f"Number of Messages extracted : {self.no_of_msg}")
            

if __name__ == "__main__":
     path = "D:/UniqueDressup/chromedriver-win64/chromedriver.exe"
     setup_driver = Driver(driver_path=path)
     print("Driver setup completed successfully.")
     name = "Manan Jain"
     access = Contact(contact_name=name)
     print("Finding contact....")
     access.find_Contact()
     print(f"Contact found: {name}")
     print("Accessing Chat....")
     extract = ChatText()
     extract.extract_messages
     print("Messages extracted successfully.")
     setup_driver.browser_exit()
     print("Browser exited successfully.")

            
        