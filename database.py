import sqlite3
import os.path

def create_connection():
    conn = None
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "database.db")
    try:
        conn = sqlite3.connect(db_path)
    except Error as e:
        print(e)
    return conn

def select_user_skills(pk):
    conn = create_connection()
    cur = conn.cursor()
    cur.execute('SELECT skills FROM skill_profiles WHERE id="{}"'.format(pk))
    data = cur.fetchone()
    res = ''.join(data)
    result = res.strip('][').split(', ')
    uri_list = [] 
    for element in result:
        cur.execute('SELECT conceptURI FROM skills_en WHERE preferredLabel={}'.format(element))
        item = cur.fetchone()
        item_str = ''.join(item)
        uri_list.append(item_str)
    return uri_list

