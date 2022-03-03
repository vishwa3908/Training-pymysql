from flask import Flask,request
import pymysql
from src.Config.connection import connect_mysql


class Subcategory:

    def show_subcategory(sub):
        try:
            conn = connect_mysql()
            mycursor = conn.cursor()
            mycursor.execute("SELECT * FROM {}".format(sub.capitalize()))
            result = mycursor.fetchall()
            if result:
                sub_category = []
                for i in range(len(result)):
                    data = {"ID":result[i][0],
                    'Item':result[i][1],
                    'Price':"Rs"+" " + str(result[i][2])}
                    sub_category.append(data)
                return {"{}".format(sub.capitalize()):sub_category}
            else:
                return "Empty"
        except:
            return "404 Error"

    def add_subcategory():
        try:
            conn = connect_mysql()
        
            mycursor = conn.cursor()
            category_name = request.json["category"].capitalize()
            check_category_value = (category_name,)
            check_category_query = '''SELECT * FROM category WHERE CATEGORY_NAME = %s'''
            mycursor.execute(check_category_query,check_category_value)
            category_result= mycursor.fetchall()
            if category_result:
                sub_category_name = request.json["sub-category"].capitalize()
                price  = request.json["price"]
                mycursor.execute('''INSERT INTO {}(ITEMS,PRICE)VALUES(%s,%s)'''.format(category_name),(sub_category_name,price))
                conn.commit()
                return "{} subcategory created".format(sub_category_name)
            else:
                return "No category Found"
        except:
            return "404 Error"

    def delete_this_subcategory():
        try:
            conn = connect_mysql()
            mycursor = conn.cursor()
            sub_category = request.json["sub-category"].capitalize()
            category = request.json["category"].capitalize()
            check_existence_value = (sub_category,)
            check_existence_query = '''SELECT * FROM {} WHERE ITEMS = %s'''.format(category)
            mycursor.execute(check_existence_query,check_existence_value)
            check_existence_result = mycursor.fetchall()
            if check_existence_result:
                delete_subcategory_value = (sub_category,)
                delete_subcategory_query = '''DELETE FROM {} WHERE ITEMS = %s'''.format(category)
                mycursor.execute(delete_subcategory_query,delete_subcategory_value)
                conn.commit()
                return "{} sub-category deleted".format(sub_category)
            else:
                return "Not Found"
        except:
            return '404 Error'