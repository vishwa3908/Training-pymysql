from flask import Flask,request,jsonify
import pymysql
from Config.connection import connect_mysql
from model.customer_cart import CustomerCart












class Login:


    def old_customer_login():
        conn = connect_mysql()
        mycursor = conn.cursor()
        name = request.json["name"].capitalize()
        password = request.json["password"]
        if name and password:
            value = (name,password,)
            query = '''SELECT * FROM customers WHERE NAME = %s AND PASSWORD = %s'''
            mycursor.execute(query,value)
            result = mycursor.fetchall()
            if result:
                data = {"Name":result[0][0],"Age":result[0][1],"Gender":result[0][2]}
                return jsonify(data)
            else:
                return "No record found"
        else:
            return "enter proper details"

    def new_customer():
        conn = connect_mysql()
        mycursor = conn.cursor()
        name = request.json["name"].capitalize()
        CustomerCart.create_cart(name)
        age = request.json["age"]
        gender = request.json["gender"].capitalize()
        password = request.json["password"]
        if name and age and gender and password:
            mycursor.execute("INSERT INTO customers(NAME,AGE,GENDER,PASSWORD)VALUES(%s,%s,%s,%s)",(name,age,gender,password))
            conn.commit()
            return {'name':name,"age":age,"gender":gender}
        else:
            return "enter all details"
    
    def delete_my_account():
        conn = connect_mysql()
        mycursor = conn.cursor()
        name = request.json["name"].capitalize()
        password = request.json["password"]
        if name and password:
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
        else:
            return "enter proper details"
