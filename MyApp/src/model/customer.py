from flask import Flask
import pymysql
from src.Config.connection import connect_mysql

class Customer:

    def create_custome_table():
        conn = pymysql.connect(
            host='localhost',
            user='vishwa',
            password='Password.123',
            database='shopping'
        )
        mycursor = conn.cursor()
        mycursor.execute("CREATE TABLE if not exists customers(ID INT AUTO_INCREMENT PRIMARY KEY,NAME VARCHAR(30),AGE INT,GENDER VARCHAR(6),PASSWORD VARCHAR(30))")