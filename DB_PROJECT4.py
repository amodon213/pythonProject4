import pymysql
from flask import Flask, request

app = Flask(__name__)

db_name = 'cReOSxv10Q'
conn = pymysql.connect(host='remotemysql.com', port=3306, user='cReOSxv10Q', passwd='iKFLyKI8Aw', db=db_name)
cursor = conn.cursor()
conn.autocommit(True)


def insert_parameter():
    name = 'alex'
    cursor.execute(f"INSERT INTO {db_name}.Dogs VALUE ({name},20,'asdasd');")


def print_table():
    cursor.execute(f"SELECT * FROM {db_name}.Dogs;")
    for row in cursor:
        print(row)


def delete_row(name):
    cursor.execute(f"DELETE FROM {db_name}.Dogs WHERE name = '{name}';")


insert_parameter()
print_table()
print("----------------------------------------------")
delete_row('adadasd')
print_table()



cursor.close()
conn.close()

"""
@app.route('/dogs')
def user():
    print("hello")
"""
