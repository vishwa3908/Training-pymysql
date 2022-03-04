from flask import Flask
import pymysql
from api.routes.endpoints.customer import mycustomer
from api.routes.endpoints.login import log_in
from api.routes.endpoints.subcategories import mysubcategory
from api.routes.endpoints.categories import mycategories
from Config.connection import connect_mysql
from model.admin import Admin
from model.category import Category
from model.customer import Customer

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
    myapp.run(debug=True,host="0.0.0.0")