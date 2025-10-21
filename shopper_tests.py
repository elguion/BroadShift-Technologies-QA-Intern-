import pytest
import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from page_objects.fashion_boutique_pages import BoutiqueHomePage, CollectionGallery, FittingRoomPage
from page_objects.test_data_manager import BoutiqueTestData

class TestBoutiqueShoppingExperience:
    """Test suite for luxury fashion boutique shopping workflow"""
    
    @pytest.fixture(autouse=True)
    def setup_teardown(self):
        """Sets up browser and test data before each test"""
        chrome_options = Options()
        chrome_options.add_argument("--window-size=1920,1080")
        chrome_options.add_argument("--disable-notifications")
        
        # Initialising WebDriver with error handling
        try:
            self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
        except Exception as e:
            pytest.fail(f"Could not initialize WebDriver: {str(e)}")
        
        self.test_data = BoutiqueTestData()
        self.customer_profiles = self.test_data.get_customer_profiles()
        self.product_variants = self.test_data.get_product_variants()
        
        yield
        
        # Capturing screenshot on failure
        if hasattr(self, '_test_outcome') and self._test_outcome.errors:
            test_name = self._test_outcome._test_method_name
            screenshot_path = f"test_reports/test_evidence/failure_{test_name}_{self.test_data.test_run_id}.png"
            self.driver.save_screenshot(screenshot_path)
            print(f"Screenshot saved: {screenshot_path}")
        
        self.driver.quit()
    
    def test_premium_shopper_complete_purchase(self):
        """Validates complete purchase flow for premium customer"""
        
        home_page = BoutiqueHomePage(self.driver)
        collection_gallery = CollectionGallery(self.driver)
        fitting_room = FittingRoomPage(self.driver)
        
        print("🧭 Starting premium shopper journey...")
        
        # Step 1: Access boutique and login
        home_page.navigate_to_boutique()
        home_page.attempt_login("standard_user", "secret_sauce")
        
        # Verification of successful login by checking inventory page loaded
        assert "inventory" in self.driver.current_url, "Login failed - not redirected to inventory"
        print("✅ Successfully accessed boutique collection")
        
        #Browse and select items
        summer_dress = self.product_variants["summer_dress"]["name"]
        collection_gallery.add_item_to_dressing_room(summer_dress)
        
        linen_pants = self.product_variants["linen_pants"]["name"] 
        collection_gallery.add_item_to_dressing_room(linen_pants)
        
        print("✅ Selected multiple fashion items for purchase")
        
        #  Proceed to checkout
        fitting_room.proceed_to_checkout()
        
        #  Fill customer information
        premium_customer = self.customer_profiles["premium_shopper"]
        fitting_room.fill_customer_details(premium_customer)
        
        #  Complete purchase
        finish_btn = self.driver.find_element(By.ID, "finish")
        finish_btn.click()
        
        # Verification of order completion
        confirmation_element = self.driver.find_element(By.CLASS_NAME, "complete-header")
        assert "Thank you for your order" in confirmation_element.text
        print("🎉 Premium shopper purchase completed successfully!")
    
    def test_guest_shopper_browse_experience(self):
        """Tests browsing experience without purchase completion"""
        home_page = BoutiqueHomePage(self.driver)
        collection_gallery = CollectionGallery(self.driver)
        
        print("👀 Starting guest shopper browsing experience...")
        
        # Access boutique with problem user to test error handling
        home_page.navigate_to_boutique()
        home_page.attempt_login("problem_user", "secret_sauce")
        
        # Verification login success
        assert "inventory" in self.driver.current_url, "Problem user login failed"
        
        #.   Attempt to interact with collections (problem_user has specific issues)
        try:
            collection_gallery.add_item_to_dressing_room("Sauce Labs Bolt T-Shirt")
            print("✅ Guest browsing interaction successful")
        except Exception as e:
            print(f"⚠️  Expected issue with problem user: {str(e)}")
        
        #  Validate cart badge updates
        cart_badge = self.driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
        assert cart_badge.text.isdigit(), "Cart badge not updating correctly"
        print(f"🛒 Cart shows {cart_badge.text} items")

def create_directory_structure():
    """Creates necessary directories for test artifacts"""
    os.makedirs("test_reports/test_evidence", exist_ok=True)
    os.makedirs("page_objects", exist_ok=True)

if __name__ == "__main__":
    create_directory_structure()
    
    # Run tests
    pytest.main([__file__, "-v", "--html=test_reports/boutique_test_report.html"])
