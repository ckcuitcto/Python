strChuoi = 'thai duc'
print(strChuoi)

chuoi = """ ádf ds " dfsghsidfg ' dà ads' " """
print(chuoi)


# chuoi nhieu dong
strChuoiNhieuDong = """ chuoi nhieu dong 
dong1
dong2 
dong 3
"""
print(strChuoiNhieuDong)


strA = 'ThaiDuc'
strB = strA[len(strA) - 1]
print(strB)

#kiem tra B cos trong A hay khong
strC = strB in strA
print(strC)

# cắt chuỗi
strD = strA[1:3]
strE = strA[1:None]
strF = strA[:None]
print(strD)
print(strE)
print(strF)


strG = strA[None:None:3]
print(strG)

# replace