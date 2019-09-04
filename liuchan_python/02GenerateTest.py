
symbols = '$µ©†®ƒç∂ß'
t = tuple(ord(symbol) for symbol in symbols)
print(t)

import array 
a = array.array('I', (ord(symbol) for symbol in symbols))
print(a)

colors = ['black', 'white']
sizes = ['S', 'M', 'L']
for tshirt in ('%s %s' % (c, s) for c in colors for s in sizes):
	print(tshirt)

