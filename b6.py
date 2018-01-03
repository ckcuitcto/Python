a = 1.96

print(a)

print(type(a))

b = 2.1234567891011121314151617

print(b)
print(type(b))

# lấy toàn bộ nội dung của thư việnc decimal
from decimal import*
# lấy tối đa 30 chữ số phần ngyên và phần thập phân decimal
getcontext().prec = 30
c = Decimal(10)/Decimal(3)
print(c)
print(type(c))
# python có phân biệt hoa thường
d = 10/3
print(d)
print(type(d))