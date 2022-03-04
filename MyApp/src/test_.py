import json
from this import d
from app import myapp


class Test:
    tester = myapp.test_client()
    data = {"name":"samuel",
        "password":"pass",
        "age":22,
        "gender":"m"}
    category_data = {"admin":"vishwa3908",
        "password":"pass1234",
        "category":"Tester"}
    sub_data = {
            "category":category_data["category"],
            "sub-category":"mytest",
            "price":200
        }
    add_cart_data = {
        "name":data["name"],
        "password":data["password"],
        "item-type":category_data["category"],
        "item":sub_data["sub-category"]
    }
    def test_1_home(self):
        response = self.tester.get("/")
        assert response.status_code==200

    def test_2_get_all_customer(self):
        response = self.tester.get("/records")
        assert response.status_code==200
        assert response.headers["Content-Type"]=="application/json"

    def test_3_new_customer(self):
        
        response = self.tester.post("/login/new",json=self.data)
        assert response.status_code==200




    def test_4_old_customer_log_in(self):
        data = {
            "name":self.data["name"],
            "password":self.data["password"]
        }
        response = self.tester.post("/login",json = data)
        assert response.status_code==200
        assert response.headers["Content-Type"]=="application/json"
        response_data = response.json
        assert response_data["Name"]==self.data["name"].capitalize()
        assert response_data["Age"]==self.data["age"]
        assert response_data["Gender"]==self.data["gender"].capitalize()


        
    def test_5_create_new_category(self):
        response = self.tester.post("/categories/add",json=self.category_data)
        assert response.status_code==200

    def test_6_show_category(self):
        response = self.tester.get("/categories")
        assert response.status_code==200
        assert response.content_type=="application/json"
        

    def test_7_add_subcategory(self):
        
        response = self.tester.post("/categories/add/subcategory",json=self.sub_data)
        assert response.status_code==200

    def test_8_show_subcategory(self): 
        response = self.tester.get("/categories/{}".format(self.sub_data["category"]))
        assert response.status_code==200
        response_data = response.json
        assert response.headers["Content-Type"]=="application/json"
        assert response_data[0]["Item"]==self.sub_data["sub-category"].capitalize()
        assert response_data[0]["Price"]=="Rs"+" "+str(self.sub_data["price"])

    def test_9_add_cart(self):
        response = self.tester.post("/records",json=self.add_cart_data)
        assert response.status_code==200

    def test_10_show_customer_cart(self):
        response = self.tester.get("/records/{}".format(self.data["name"]))
        assert response.status_code==200
        assert response.headers["Content-Type"]=="application/json"
        response_data = response.json
        assert response_data[0]["Item"]==self.sub_data["sub-category"].capitalize()
        assert response_data[0]["Item-Type"]==self.sub_data["category"].capitalize()
        assert response_data[0]["Price"]==self.sub_data["price"]


    def test_11_delete_cart(self):
        delete_data = self.add_cart_data

        response = self.tester.delete("/records",json=delete_data)
        assert response.status_code==200

    def test_12_delete_subcategory(self):
        del_sub_data = {
            "category":self.category_data["category"],
            "sub-category":self.sub_data["sub-category"]
        }
        response = self.tester.delete("/categories/delete/subcategory",json = del_sub_data)
        assert response.status_code==200

    def test_13_delete_category(self):
        del_cat_data = self.category_data
        response = self.tester.delete("/categories/delete",json=del_cat_data)
        assert response.status_code==200


    def test_14_delete_customer_account(self):
        data = {
            "name":self.data["name"],
            "password":self.data["password"]
        }
        response = self.tester.delete("/login/delete",json=data)
        assert response.status_code==200