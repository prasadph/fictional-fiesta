from sys import argv
import MySQLdb
from begin import start

def available():
    user_id = 1
    db = MySQLdb.connect("localhost", "root", "root", "reviews")
    cursor = db.cursor()
    try:
        sql = "SELECT status from user where user_id="+ user_id
        # print sql
        cursor.execute(sql)
        results = cursor.fetchall()
        if results[0] == 'empty':
            pass
        elif result[0] ==  'uploaded':
            start(user_id +".csv")

    except MySQLdb.Error as e:
        print e
        db.rollback()
