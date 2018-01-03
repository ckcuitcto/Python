tup = (i for i in range(10) if i% 2 == 0)
a = tuple(tup)
a *= 2

a += (1,3,5)
print(a)

b = a[3]
print(b)

a = ((1,3,4,5,6),3,4,5)

b = a.count(5)
print(b)

tup = (1, 2, [3, 4])

print(tup)