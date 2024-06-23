import sqlite3

def create_subscribed_users_storage():
    conn = sqlite3.connect("subscribed_users.db")
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='users'")
    result = cursor.fetchone()
    if result:
        print("TABLE users already created")
    else:
        print("Create table")
        cursor.execute("CREATE TABLE users(id INTEGER)")
    conn.close()

def add_subscribed_user(user_id):
    conn = sqlite3.connect("subscribed_users.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users VALUES (?)",(user_id,))
    conn.commit()
    conn.close()

def remove_subscribed_user(user_id):
    conn = sqlite3.connect("subscribed_users.db")
    cursor = conn.cursor()
    cursor.execute("DELETE from users WHERE id = ?",(user_id,))
    conn.commit()
    conn.close()

def check_subscription(user_id):
    conn = sqlite3.connect("subscribed_users.db")
    cursor = conn.cursor()
    check = cursor.execute("SELECT id FROM users WHERE id = ?",(user_id,))
    if check.fetchone() is None:
        conn.close()
        return False
    conn.close()
    return True

def database_dump():
    conn = sqlite3.connect("subscribed_users.db")
    cursor = conn.cursor()
    for id in cursor.execute("SELECT id FROM users"):
        print(id[0])
    conn.close()

def getSubscribedUserIDS():
    conn = sqlite3.connect("subscribed_users.db")
    cursor = conn.cursor()
    res = cursor.execute("SELECT id FROM users")
    ids = res.fetchall()
    conn.close()
    return ids
    