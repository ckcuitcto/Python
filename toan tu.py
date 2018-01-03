n = 69

n.__add__(1) # tương tự khi bạn n + 1
print(n.__add__(1))

print(n.__sub__(9)) # tương tự n - 9

n.__mul__(2)  # tương tự n * 2
print(n.__mul__(2))

n.__radd__(1)  # tương tự 1 + n
print(n.__radd__(1))

n.__rsub__(9) # tương tự 9 - n
print(n.__rsub__(9))

n.__neg__() # tương tự -n
print(n.__neg__())