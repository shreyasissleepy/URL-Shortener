import sqlite3

def store(target, shortid):
    try:
        conn = sqlite3.connect('urlshort.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO USER (target, shortid) VALUES (?, ?)", (target, shortid))
        conn.commit() 
        return 'success'
    except sqlite3.IntegrityError:
        return 'shortid already exists'
    finally:
        cursor.close()
        conn.close()


def find(shortid):
    try:
        conn = sqlite3.connect('urlshort.db')
        cursor = conn.cursor()
        cursor.execute("SELECT target FROM USER WHERE shortid = ?", (shortid,))
        result = cursor.fetchone()
        if result:
            return result[0]
        else:
            return None
    finally:
        cursor.close()
        conn.close()
