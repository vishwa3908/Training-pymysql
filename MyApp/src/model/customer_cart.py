from flask import Flask
import pymysql
from src.Config.connection import connect_mysql

class CustomerCart:
    
    def create_cart(name):
        conn = connect_mysql()
        mycursor = conn.cursor()
        mycursor.execute("CREATE TABLE IF NOT EXISTS {}(ITEM_TYPE VARCHAR(20) , ITEM VARCHAR(33),QUANTITY INT DEFAULT 1 ,PRICE INT,TOTAL INT)".format(name.capitalize()))
        
    
    def add_customercart():
        pass