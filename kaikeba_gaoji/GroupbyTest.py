
rows = [
	{'address' : '5412 N CLARK', 'date' : '07/01/2012'},
	{'address' : '5413 N CLARK', 'date' : '07/04/2012'},

	{'address' : '5412 E TErrST', 'date' : '07/02/2012'},
	{'address' : '5412 E 34TEST', 'date' : '07/03/2012'},

	{'address' : '4215 N FDSFFDS', 'date' : '07/02/2012'},
	{'address' : '4215 N SDFFSDF', 'date' : '07/05/2012'},

	{'address' : '2342 N FDSFS33', 'date' : '07/04/2012'},
	{'address' : '2312 N 34343', 'date' : '07/03/2012'},

]


from operator import itemgetter
from itertools import groupby

rows.sort(key=itemgetter('date'))

for date, items in groupby(rows, key = itemgetter('date')):
	print(date)
	for i in items:
		print('  ', i)


print("-" * 50)

from collections import defaultdict
rows_by_date = defaultdict(list)

for row in rows:
	rows_by_date[row['date']].append(row)


for r in rows_by_date['07/04/2012']:
	print(r)