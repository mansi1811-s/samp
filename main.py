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
