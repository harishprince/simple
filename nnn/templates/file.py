from string import maketrans   

intab = "aeiou"
outtab = "12345"
trantab = maketrans(intab, outtab)

str = "hello"
print str.translate(trantab)

# a = ['a', 'b', 'c', 'd', 'e', 'f']
# print a[1:5:2]