from flask import Flask
import pymysql
from src.api.routes.endpoints.customer import mycustomer
from src.api.routes.endpoints.login import log_in
from src.api.routes.endpoints.subcategories import mysubcategory
from src.api.routes.endpoints.categories import mycategories
from src.Config.connection import connect_mysql
from src.model.admin import Admin
from src.model.category import Category
from src.model.customer import Customer

myapp = Flask(__name__)
myapp.register_blueprint(mycustomer)
myapp.register_blueprint(mycategories)

myapp.register_blueprint(log_in)
myapp.register_blueprint(mysubcategory)
def connection():
    conn = pymysql.connect(
        host='localhost',
        user='vishwa',
        password='Password.123',
        database='shopping'
    )
    mycursor = conn.cursor()
@myapp.route("/")
def home():
    connection()
    Admin.create_admin()
    Category.create_category()
    Customer.create_custome_table()

    return "WELCOME TO SHOPPING "
if __name__=="__main__":
    myapp.run(debug=True)