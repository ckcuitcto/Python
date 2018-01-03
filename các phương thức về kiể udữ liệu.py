a = 'thái Huỳnh đức'
b = a.capitalize()
c = a.upper()
d = a.lower()
e = a.swapcase()
f = a.title()

g = a.center(20)
h = a.center(20,'-')
i = a.ljust(20,'@')
# rjust

# print(b)
# print(c)
# print(d)
# print(e)
# print(f)
# print(g)
# print(h)
# print(i)


str = ' chuoi '
b = str.join(['1','2','3','4','5'])
print(b)

chuỗicầnthaythế = ' giá trị của chuỗi'
# gía trị thứ 3 là số lượng thay thế
b = chuỗicầnthaythế.replace('i', 'j',1)
print(b)

# bỏ các kí tự ở đầu và cuối chuỗi nếu giống trong ngoặc
chuoi = 'aa bbcc aa'
b = chuoi.strip('aa')
# con co lstrip va rstrip
print(b)

#split
a = 'thai huynh duc huynh '
b = a.split(' ',2)
print(b)


#partition
b = a.rpartition('huynh')
print(b)

#count
# 0-14 là vị trí từ khí tự thứ mấy đến thứ mấy
b = a.count('huynh',0,14)
print(b)

#startswith
# bắt đầu chuỗi là gì
b = a.startswith('thai')
print(b)

c = a.startswith('huynh',5)
print(c)

#find
b = a.find('huy1nh')
print(b)

#index . giiống find nhưng nếu tìm kthấy sẽ báo lỗi
b = a.index('huynh')
print(b)

# islowwer ,isupper ,
# isdigit kiểm tra có phải là số hay không
b = a.isdigit()
print(b)
#idspace tra ve neu chuoi la khoang trang


s = 'aaaAAaaaooaaneu mot Ngay naO Doaaaaaaa'
s = s.lower()
s = s.strip('a')
s = s.lstrip('o')
s = s.lstrip('a')
s = s.title()
print(s)