# Snapdeal
# http://www.snapdeal.com/product/htc-one-a9-32gb-4g/656270477475
# http://www.snapdeal.com/product/htc-one-a9-32gb-4g/656270477475/reviews?rateFilter=3&page=1

import requests
from pyquery import PyQuery as pq
import sys
import json

def snapdeal(url):     
    r = requests.get(url)
    url = str(r.url)
    pid = url.split('/')[-1]
    base_rev_url = url + '/reviews?'
    pname = url.split('/')[3]
    rating = 3
    start = 1
    tp_url = 'http://text-processing.com/api/sentiment/'

    while rating >= 1:
        page_url = base_rev_url + 'rateFilter=' + str(rating) + '&page=' + str(start)
        rev_page = requests.get(page_url)
        print '\nFetched rate ' + str(rating) + ' page ' + str(start)
        d = pq(rev_page.content)
        if len(d('div.text div.user-review p')) == 0:
            # print d('title')
            # exit()
            rating = rating - 1
            start = 1
            # print "\nNo reviews dude"
            # No review go to next rating
        else:
            start = start + 1
            # print "review"
            reviews = d('div.text div.user-review p')
            # print 'jale'
            for rev in reviews:
                payload = {'text':rev.text_content()}
                j = requests.post(tp_url,data=payload)
                json_data = j.json()
                yield(pid,rev.text_content(),json_data['probability']['neg'])