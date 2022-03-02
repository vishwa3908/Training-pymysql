from flask import Flask
import pymysql
from src.Config.connection import connect_mysql


class Category:

    def create_category():
        conn = pymysql.connect(
            host='localhost',
            user='vishwa',
            password='Password.123',
            database='shopping'
        )
        mycursor = conn.cursor()
        mycursor.execute("CREATE TABLE if not exists category(CATEGORY_NAME VARCHAR(30) PRIMARY KEY)")