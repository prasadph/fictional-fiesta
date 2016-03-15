# http://www.flipkart.com/item/PLOEBP45AY3YZJHG
# http://www.flipkart.com/renka-turtle-neck-solid-women-s-pullover/p/itmebp45tzffzpjd?pid=PLOEBP45AY3YZJHG
# http://www.flipkart.com/renka-turtle-neck-solid-women-s-pullover/product-reviews/ITMEB9AGNNA2THPA?pid=PLOEBP45AY3YZJHG&rating=3
# for page 2 and so on
# http://www.flipkart.com/renka-turtle-neck-solid-women-s-pullover/product-reviews/ITMEB9AGNNA2THPA?pid=PLOEBP45AY3YZJHG&rating=3&start=10 
# 
# http://www.flipkart.com/renka-turtle-neck-striped-women-s-pullover/p/itmebp45cdhttnzt?pid=PLOEBP46M9WNTEPP
# http://www.flipkart.com/renka-turtle-neck-striped-women-s-pullover/product-reviews/ITMEB9AGNNA2THPA?pid=PLOEBP46M9WNTEPP&rating=3

# Snapdeal
# http://www.snapdeal.com/product/htc-one-a9-32gb-4g/656270477475
# http://www.snapdeal.com/product/htc-one-a9-32gb-4g/656270477475/reviews?rateFilter=3&page=1


import requests
from pyquery import PyQuery as pq
from reviews import review
import json

def flipkart(db_url):
    # For testing. review wala link
    # pname = 'http://www.flipkart.com/oneplus-one/p/itme87deqpethtwa?pid=MOBE87BTKJY8QYZH'
    # pid = 'MOBE87BTKJY8QYZH'

    # db_url = 'http://www.flipkart.com/item/MOBE87BTKJY8QYZH'
    r = requests.get(db_url)
    pname = r.url
    pname = str(pname)
    pname = pname.split('/')[3]
    pid = db_url.split('/')[-1]
    tp_url = 'http://text-processing.com/api/sentiment/'

    rating = 3
    start = 0
    num = 1
    base_rev_url = 'http://www.flipkart.com/' + pname + '/product-reviews/ITMEB9AGNNA2THPA?pid=' + pid + '&rating='

    while rating >= 1:
        rev_page = requests.get(base_rev_url + str(rating) + '&start=' + str(start))
        print '\nFetched rate ' + str(rating) + ' page ' + str(start/10+1)
        d = pq(rev_page.content)
        x = d('.fk-review-page.gd-row.newvd').html()
        if x is not None:
            if 'No reviews found.' in x:
                rating = rating - 1
                start = 0
                # print "\nNo reviews dude"
                # No review go to next rating
            else:
                start = start + 10
                reviews = d('.review-text')
                for rev in reviews:
                    payload = {'text':rev.text_content()}
                    j = requests.post(tp_url,data=payload)
                    json_data = j.json()
                    yield (pid,rev.text_content(),json_data['probability']['neg'])