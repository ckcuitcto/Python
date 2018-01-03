list1 = [[1,2,3],[4,5,6],['asd',3,'dfd'],[123,3.5,'545']]
print(list1[0])

a = [i for i in range(10)]
print(a)

b = [[n,n*1,n*2] for n in range(1,3)]
print(b)

c = list('ccc')
print(c)

a = [1,2]
a += ['one','two']
print(a)

b = [1,2]
b *=3
print(b)

a = [1,2]
b = '1' in a
print(b)

a = [1,2,3,'a','b','c',[4,5]]
print(a[6])

b = a[::-1]
print(b)

c = list(a)
c[1] = 'aaaa'
print(a)
print(c)


a = [1,2,1,4,56,7,8,9]
b = a.index(9)
# trả về trị trí của giá trị trong index trong bảng
print(b)

#clear de xoa. copy de copy
a.append([4,5])
print(a)
a.extend([6,7])
print(a)

# them phan tu 9 o vi tri 0
a.insert(0,9)
print(a)

# xoa phan tu o vi tri thu..
a.pop(0)
print(a)

# xoa phan tu co gia tri...
a.remove(1)
print(a)

# sap xep
a = [9,4,6,8,2,1]
a.sort(reverse=True)
print(a)

