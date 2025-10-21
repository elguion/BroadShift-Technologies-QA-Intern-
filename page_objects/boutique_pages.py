from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class BoutiqueHomePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    def navigate_to_boutique(self):
        """Opens the fashion boutique homepage"""
        self.driver.get("https://www.saucedemo.com/")  # Using demo site as example
        
    def attempt_login(self, username, password):
        """Attempts to login with provided credentials"""
        username_field = self.wait.until(EC.element_to_be_clickable((By.ID, "user-name")))
        username_field.send_keys(username)
        
        password_field = self.driver.find_element(By.ID, "password")
        password_field.send_keys(password)
        
        login_btn = self.driver.find_element(By.ID, "login-button")
        login_btn.click()

class CollectionGallery:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)
    
    def select_designer_collection(self, collection_name):
        """Selects a specific designer collection"""
        collection_locator = f"//div[contains(@class, 'inventory_item_name') and contains(text(), '{collection_name}')]"
        collection_item = self.wait.until(EC.element_to_be_clickable((By.XPATH, collection_locator)))
        collection_item.click()
    
    def add_item_to_dressing_room(self, item_name):
        """Adds item to cart/dressing room"""
        add_to_cart_btn = self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, f"//div[contains(text(), '{item_name}')]/ancestor::div[@class='inventory_item']//button")))
        add_to_cart_btn.click()
        return f"Added {item_name} to dressing room"

class FittingRoomPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    def proceed_to_checkout(self):
        """Navigates to checkout process"""
        cart_icon = self.driver.find_element(By.CLASS_NAME, "shopping_cart_link")
        cart_icon.click()
        
        checkout_btn = self.wait.until(EC.element_to_be_clickable((By.ID, "checkout")))
        checkout_btn.click()
    
    def fill_customer_details(self, customer_data):
        """Fills customer information during checkout"""
        fields = {
            "first-name": customer_data["name"].split()[0],
            "last-name": customer_data["name"].split()[1],
            "postal-code": "10001"
        }
        
        for field_id, value in fields.items():
            field = self.wait.until(EC.element_to_be_clickable((By.ID, field_id)))
            field.send_keys(value)
        
        continue_btn = self.driver.find_element(By.ID, "continue")
        continue_btn.click()
