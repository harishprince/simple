d={'a':1,'b':2}
res = dict((v,k) for k,v in d.iteritems())
print res

a="hello"
for i in a:
	b=ord(i)-32
	c=chr(b)
	print c	

d={'a':1,'b':2}
c=dict(zip(d.values(),d))
print c
	