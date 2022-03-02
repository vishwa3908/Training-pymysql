import unittest
from urllib import response
import requests
from app import myapp

class Login_check(unittest.TestCase):
    data = {
            "name" : "vishwa",
            "age" : 22,
            "password" : "pass",
            "gender" : "M"}
    check_data = {
        "name":"vishwa",
        "password":"pass"
                    }
# Customer Side
     
# ---------new customer entry check------
   
    def test_case_1_new_customer_post(self):
        tester = myapp.test_client()
        response = tester.post("/login/new",json=self.data)
        self.assertEqual(response.status_code,200)

#------------old customer check-------------

    def test_case_2_old_customer_post(self):
        tester = myapp.test_client()
        response = tester.post("/login",json = self.check_data)
        self.assertEqual(response.status_code,200)

#-------- customer account delete check-------  
    def test_case_3_delete_customer_delete(self):
        tester = myapp.test_client()
        response = tester.delete("/login/delete",json =self.check_data)
        self.assertEqual(response.status_code,200)