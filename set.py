set_1 = {69,96}
print(type(set_1))

set_2 = {'thai duc'}
print(set_2)

set_3 = {(3,2,'thai duc'),(3,2.3)}
print(set_3)

set4 = {value for value in range(4)}
print(set4)
print(type(set4))

# set k co gia tri trung lap
set5 = set('aaaaaaaaaa')
print(set5)
print(type(set5))

set5 = set([1,3,4,5,6,2,1,4,6,6])
print(set5)
print(type(set5))

set6 = set()
# print(set6)
#
# print(1 in {1,3,4})
#
# print(1,2,3 in {1,2,4,5,6,6})
#
# print({1,2,3} - {4,2,1})
#
# print({1,2,3} - {4,2,1})
#
# # & ca 2 ben deu co
# print({1,2,3} & {1,4})
#
# # | lay het 2 ben
# print({1,2,3} | {4,2,3,6,7})
#
# # ^ lay het cua 2 ben, loai het cai trung nhau
# print({1,2,3} ^ {4,2,3,6,7})

print(set5)
set5.remove(2)
# có thể dùng discart để xoá tương tự remove nhưng nếu k có sẽ k  báo lỗi như remove
print(set5)

set5.discard(4)
print(set5)

set6 = set5.copy()
print(set6)

set6.add(2)
print(set5)
print(set6)