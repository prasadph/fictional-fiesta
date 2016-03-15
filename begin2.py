# 'http://www.flipkart.com/item/MOBE87BTKJY8QYZH'
# 'http://www.snapdeal.com/product/page/639082261977'

from snapdealstuff import snapdeal
from flipkart import flipkart
from reviews import review
from csvthingy import links

for link in links('renka_product_url_fk_snapdeal.csv'):
	for rev in flipkart(link[1]):
		print rev
	for rev in snapdeal(link[2]):
		print rev