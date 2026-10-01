#import sqlite3

DB_NAME = "clientele.db"

def create_database():
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
    )
""")
    connection.commit()
    connection.close()

def register_user(username, password):
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()

    try:
        cursor.execute("""
        INSERT INTO users (username, password)
        VALUES (?,?)
        """, (username, password))
        connection.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        connection.close()

def check_user(username, password):
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()

    cursor.execute("""
    SELECT id
    FROM users
    WHERE username = ? AND password = ?
    """, (username, password))
    user = cursor.fetchone()
    connection.close()
    return user is not None
