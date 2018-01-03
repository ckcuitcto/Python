dic = {'name':'thai duc','member':69}
print(dic)

print(type(dic))

dic1  = { key:value for key,value in [('name','thai'),('member',69)]}
print(dic1)


name = 'SpaceX'
member = 696969
dic = dict(name='Kteam', member=69)
print(dic)
print(name)
print(member)


iterable =  ('name','number', True ,23)
dic_none = dict.fromkeys(iterable)
print(dic_none)
#  mặc định là None . có thể thay = giá trị khác = cách dươis
dic = dict.fromkeys(iterable , ' thay giá trị none = giá trị khác')
# print(dic)
print(dic['number'])
dic['number'] = 99999
print(dic['number'])
print(dic)

dic = dict(duc = 'thai duc',sdt = 123)
dic['sdt'] = dic['sdt'] + 1
print(dic)
# neu gan 1 key chua ton tai. no se tu them vao
dic['aaa'] = 'aaa'
print(dic)

d = {'Team': 'Kteam', (1,2):68}
print(d)

# d.clear();
# print(d)

value = d.get('Team')
value1 = d.get((1,2))
print(value)
print(value1)

value2 = d.get('aaaa',' giá trị mặc định nếu gọi ra k có ')
print(value2)

#items Trả về một giá trị thuộc lớp dict_items. Các giá trị của dict_items sẽ là một tuple với giá trị thứ nhất là key, giá trị thứ hai là value.
value3 = d.items()
print(value3)
list_items = list(value3)
print(list_items[0])

#keys Trả về một giá trị thuộc lớp dict_keys. Các giá trị của dict_keys sẽ là các key trong Dict.
value4 = d.keys()
print(value4)

# pop . Công dụng: Bỏ đi phần tử có key và trả về value của key đó. Trường hợp key không có trong dict.
# Báo lỗi KeyError nếu default là None (ta không thêm vào).
# Trả về default nếu ta thêm default vào.

# value5 = d.pop('Team')
# print(value5)
# print(d)

value6 = d.pop('abc' ,' gia tri mac dinh hien thi neu k tim thay key, neu k co gia tri nay thi se bao loi')
print(value6)
print(d)

#setdefautl
# Trả về giá trị của key trong Dict. Trường hợp key không có trong Dict thì sẽ trả về giá trị default.
# Thêm nữa, một cặp key-value mới sẽ được thêm vào Dict với key bằng key và value bằng default.

d.setdefault('keyDefault',' gia tri cua key default')
print(d)
value7 = d.get('aaaaa')
print(value7)

# update . se them vao cac gia tri. neu key da ton tai thi se thay the noi dung
d = {'a': 1}
d.update(b=2, c='32dasf a3')
print(d)

tuple1 = [('b', 4), ('c', 3)]
d.update(tuple1)
print(d)

# d.update({'a': 3})
# print(d)

dict1 = {'key': 6969}
print(dict1)
dict2 = dict1.copy()
dict2['key'] = 'changed'
print(dict2)
print(dict1)