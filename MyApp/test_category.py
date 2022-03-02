import requests
import unittest

from app import myapp

class category_test(unittest.TestCase):
    data = {
            "admin":"vishwa3908",
            "password":"pass1234",
            "category":"gaming"
        }
    
    def test_case_9_show_category(self):
        tester = myapp.test_client()
        response = tester.get("/categories")
        self.assertEqual(response.status_code,200)
        self.assertEqual(response.content_type,"application/json")
        
    def test_case_10_add_category(self):
        tester = myapp.test_client()
        response = tester.post('/categories/add',json = self.data)
        self.assertEqual(response.status_code,200)
        
    def test_case_11_delete_category(self):
        tester = myapp.test_client()
        response = tester.delete('/categories/delete',json = self.data)
        self.assertEqual(response.status_code,200)

if __name__ == "__main__":
    unittest.main()
        