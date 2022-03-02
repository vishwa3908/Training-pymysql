import unittest
from urllib import response
import requests
from app import myapp


class Customer_check(unittest.TestCase):
    add_cart_data = {
        "name":"vishwa",
        "password":"pass",
        "item-type":"mobile",
        "item":"lava"
    }
 
# ---------------------------check all records -----       
    def test_case_4_get(self):
        tester = myapp.test_client()
        response = tester.get("/records")
        self.assertEqual(response.status_code,200)
        
    #---- checking response format---------
    def test_case_5_check_get_response(self):
        tester = myapp.test_client()
        response = tester.get("/records")
        self.assertEqual(response.content_type,"application/json")
        
        

    # --------------add customer cart---------
   
    def test_case_6_add_cart(self):
        tester = myapp.test_client()
        response = tester.post("/records",json=self.add_cart_data)
        self.assertEqual(response.status_code,200)

    #----show cart --------
    def test_case_7_show_cart(self):
        tester = myapp.test_client()
        response = tester.get("/records/Vishwa")
        self.assertEqual(response.status_code,200)
        
    #-- delete cart check--------
    def test_case_8_delete_cart(self):
        tester = myapp.test_client()
        response = tester.delete("/records",json = self.add_cart_data)
        self.assertEqual(response.status_code,200)
    
        
    

if __name__ == "__main__":
    unittest.main()
