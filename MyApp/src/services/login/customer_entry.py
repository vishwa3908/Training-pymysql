from flask import Flask,request
import pymysql
from src.Config.connection import connect_mysql
from src.model.customer_cart import CustomerCart












class Login:


    def old_customer_login():
        try:
            conn = connect_mysql()
            mycursor = conn.cursor()
            name = request.json["name"].capitalize()
            password = request.json["password"]
            value = (name,password,)
            query = '''SELECT * FROM customers WHERE NAME = %s AND PASSWORD = %s'''
            mycursor.execute(query,value)
            result = mycursor.fetchall()
            if result:
                data = {"Name":result[0][0],"Age":result[0][1],"Gender":result[0][2]}
                return data
            else:
                return "No record found"
        except:
            return "404 error"

    def new_customer():
        try:
            conn = connect_mysql()
            mycursor = conn.cursor()
            name = request.json["name"].capitalize()
            CustomerCart.create_cart(name)
            age = request.json["age"]
            gender = request.json["gender"].capitalize()
            password = request.json["password"]
            mycursor.execute("INSERT INTO customers(NAME,AGE,GENDER,PASSWORD)VALUES(%s,%s,%s,%s)",(name,age,gender,password))
            conn.commit()
            return {'name':name,"age":age,"gender":gender}
        except:
            return "Error 404"
    
    def delete_my_account():
        try:
            conn = connect_mysql()
            mycursor = conn.cursor()
            name = request.json["name"].capitalize()
            password = request.json["password"]
            value = (name,password,)
            query = '''SELECT * FROM customers WHERE NAME = %s AND PASSWORD = %s'''
            mycursor.execute(query,value)
            result = mycursor.fetchall()
            if result:
                delete_value = (name,password,)
                delete_query = "DELETE FROM customers WHERE NAME=%s AND PASSWORD = %s"
                mycursor.execute(delete_query,delete_value)
                conn.commit()
                mycursor.execute("DROP TABLE IF EXISTS {}".format(name))
                conn.commit()
                return "record deleted"
            else:
                return  "record not found"
        except:
            return "404"
