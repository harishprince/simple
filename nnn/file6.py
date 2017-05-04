# a="hello"
# b=len(a)
# print b
# b=a.capitalize()
# print b

# a="bangalore"
# a.encode('base64','strict');
# print a

# a = "bangalore";
# a = a.encode('base64','strict');

# print "Encoded String: " + a
# print "Decoded String: " + a.decode('base64','strict')

# a="mangalore"
# print a.count('a')

# a="python"
# print a[:1]+a[1:2].upper()+a[2:3]+a[3:4].upper()+a[4:5]+a[5:6].upper()

l = ['amar',1,'rag','pran',2,3]
a=[]
b=[]
for i in l:
	if type(i)!=type(10):
		a.append(i)
		print a,
	else:
		b.append(i)	
		print b,		
