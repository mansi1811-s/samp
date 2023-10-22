# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
# from flask import Flask
# import boto
# from boto.s3.key import Key
# AWS_ACCESS_KEY_ID = 'ABCD11EFGHIJK'
# AWS_SECRET_ACCESS_KEY = 'HUIHUGhuu898ERUGHIUHSIUHH'

# # Flask constructor takes the name of 
# # current module (__name__) as argument.
# app = Flask(__name__)

# # The route() function of the Flask class is a decorator, 
# # which tells the application which URL should call 
# # the associated function.
# @app.route('/')
# # ‘/’ URL is bound with hello_world() function.
# def hello_world():
# 	print(AWS_SECRET_ACCESS_KEY)
# 	return 'Hello World'

# # main driver function
# if __name__ == '__main__':

# 	# run() method of Flask class runs the application 
# 	# on the local development server.
# 	app.run()

import sqlite3

def get_user_data(username):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    #Correct code without vulnerability
    # query = "SELECT * FROM users WHERE username = ?"

    #Directly concatenating user input into SQL query -CVE-2018-6829
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    cursor.execute(query)

    user_data = cursor.fetchall()
    conn.close()
    return user_data

username = input("Enter a username: ")
user_data = get_user_data(username)
print(user_data)
