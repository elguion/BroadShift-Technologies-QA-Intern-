import json
import openpyxl
from datetime import datetime

class BoutiqueTestData:
    
    
    def __init__(self):
        self.test_run_id = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    def get_customer_profiles(self):
        """Returns different customer types for testing"""
        return {
            "premium_shopper": {
                "name": "Eleanor Vance",
                "email": f"eleanor.vance{self.test_run_id}@stylemail.com",
                "newsletter_pref": True
            },
            "budget_shopper": {
                "name": "Marcus Chen",
                "email": f"marcus.chen{self.test_run_id}@stylemail.com", 
                "newsletter_pref": False
            }
        }
    
    def get_product_variants(self):
        """Returns product test data"""
        return {
            "summer_dress": {
                "name": "Sahara Summer Dress",
                "size": "M",
                "color": "Coral Sunset"
            },
            "linen_pants": {
                "name": "Mediterranean Linen Trousers", 
                "size": "32",
                "color": "Navy Blue"
            }
        }
