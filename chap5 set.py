a = {2, 4, 7, 8, 6}

print(a)
print(type(a))
# Empty set

a = {}
print(type(a)) # this is an empty dictionary not an empty set.

# Empty set

b = set()
# adding an elementsset
b.add(0)
b.add(1)
b.add(2)
b.add(3)
b.add(4)
b.add(5)  # adding a value repedatelt doesnt change a set
b.add((5, 4, 7, 9))
print(b)
print(type(b))

print(len(b))  # tell the lenght of the set

b.remove(5)

print(b)

print(b.pop())
print(b)