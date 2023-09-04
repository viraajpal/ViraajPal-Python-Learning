
#  In Python integer nd floating values are count as same so only pne value will be count

s = set()
s.add(20)
s.add(20.0)
s.add("20")
print(len(s))



