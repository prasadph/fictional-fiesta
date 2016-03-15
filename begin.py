from snapdealstuff import snapdeal
from flipkart import flipkart
from reviews import review
import MySQLdb
from csvthingy import links

def insert(product_id, skuid, reviews, score, user_id):
    db = MySQLdb.connect("localhost", "root", "root", "reviews")
    cursor = db.cursor()
    try:
        sql = "INSERT into product (product_id, skuid, reviews,score,user_id) values ('{0}',{1},{2},{3},{4})".format(product_id, skuid, repr(reviews),score,user_id)
        # print sql
        print reviews
        cursor.execute(sql)
        db.commit()
    except MySQLdb.Error as e:
        print e
        db.rollback()


def complete(user_id):
    db = MySQLdb.connect("localhost", "root", "root", "reviews")
    cursor = db.cursor()
    try:
        sql = "UPDATE user SET status='complete' where user_id=" + str(user_id)
        # print MySQLdb
        cursor.execute(sql)
        db.commit()
    except MySQLdb.Error as e:
        print e
        db.rollback()


def clear(user_id):
    db = MySQLdb.connect("localhost", "root", "root", "reviews")
    cursor = db.cursor()
    try:
        sql = "DELETE from product where user_id={0}".format(user_id)
        # print sql
        cursor.execute(sql)
        db.commit()
    except MySQLdb.Error as e:
        print e
        db.rollback()

def start(filename):
    user_id = 1
    product_id = "1"
    skuid = 1
    reviews = "dsadas'dsd"
    score = 1.1
    clear(user_id)
    # insert(product_id, skuid, reviews, score, user_id)

    # for link in links('renka_product_url_fk_snapdeal.csv'):
    for link in links(filename):
        for rev in flipkart(link[1]):
            product_id = rev[0]
            skuid = link[0]
            reviews = rev[1]
            score = rev[2]
            user_id = 1
            insert(product_id, skuid, reviews, score, user_id)
        for rev in snapdeal(link[2]):
            product_id = rev[0]
            skuid = link[0]
            reviews = rev[1]
            score = rev[2]
            user_id = 1
            insert(product_id, skuid, reviews, score, user_id)
