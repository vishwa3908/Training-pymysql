
from flask import Flask,request,jsonify
import pymysql
from Config.connection import connect_mysql
from model.customer_cart import CustomerCart












class Login:


    def old_customer_login():
        conn = connect_mysql()
        mycursor = conn.cursor()
        id = request.json["id"]
        name = request.json["name"].capitalize()
        password = request.json["password"]
        if id and name and password:
            value = (id,name,password,)
            query = '''SELECT * FROM customers WHERE ID = %s AND NAME = %s AND PASSWORD = %s'''
            mycursor.execute(query,value)
            result = mycursor.fetchall()
            if result:
                data = {"Id":result[0][0],"Name":result[0][1],"Age":result[0][2],"Gender":result[0][3]}
                return jsonify(data)
            else:
                return jsonify("No record found")
        else:
            return jsonify("enter all details")

    def new_customer():
        conn = connect_mysql()
        mycursor = conn.cursor()
        id = request.json["id"]
        if id>99999 or id <1:
            return jsonify("enter id between 1 and 99999")
        else:
            name = request.json["name"].capitalize()
            CustomerCart.create_cart(name)
            age = request.json["age"]
            gender = request.json["gender"].capitalize()
            password = request.json["password"]
            if id and name and age and gender and password:
                mycursor.execute("SELECT ID FROM customers")
                result = mycursor.fetchall()
                result = list(result)
                print(result)
                for i in result:
                    if id==i[0]:
                        return jsonify("Enter different id")
                else:

                    mycursor.execute("INSERT INTO customers(ID,NAME,AGE,GENDER,PASSWORD)VALUES(%s,%s,%s,%s,%s)",(id,name,age,gender,password))
                    conn.commit()
                    return jsonify({"id":id,'name':name,"age":age,"gender":gender})
            else:
                return jsonify("enter all details")
    
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
                return jsonify("record deleted")
            else:
                return  jsonify("record not found")
        else:
            return jsonify("enter all details")
