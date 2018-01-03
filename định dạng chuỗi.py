a = ' Thay the chuoi %s %d ahah ' %('ád',2)
print(a)

name = 'thai duc'
lop = 'd14 th01'
sdt = '123654254'

resutl = f'ten hoc sinh: {name} \n lop :{lop} \n \t sdt :{sdt} '
print(resutl)


r = '1: {1} , 2:{0}  '.format(111,222)
print(r)


bb = 'aa'
cc = 'bb'
dd = 2
chuoi = 'chu va so deu dc :{b} , {c},{d}'.format(b=bb,c=cc,d=dd)
print(chuoi)

# căn lề < > ^ 
ee = '{:@<20}'.format('Thai duc')
print(ee)