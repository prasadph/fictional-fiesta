import csv

def links(thefile):
	with open(thefile) as csvfile:
		rows = csv.reader(csvfile, delimiter=',')
		for row in rows:
			if 'sku_id' not in row[1]:
				yield(row[1],row[2],row[3]) 