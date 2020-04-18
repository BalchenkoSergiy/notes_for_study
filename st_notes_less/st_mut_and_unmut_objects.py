# **********************************************************************************************************************
# **********************************************************************************************************************
# Lesson 17 'Mutable and nonmutable objects'
print('***************************************************************************************************************')

x = 10
print(x, id(x)) # 10 140710333232240

x = 20
print(x, id(x)) # 20 140710333232560

print('***************************************************************************************************************')

s = 'hello'
print(s, id(s)) # hello 3060503049808
s += ' world'
print(s, id(s)) # hello world 3060505905968

print('***************************************************************************************************************')

l = [1, 2, 3]
print(l, id(l)) # [1, 2, 3] 1647586599496
l.append(5)
print(l, id(l)) # [1, 2, 3, 5] 1647586599496

print('***************************************************************************************************************')

x = 10
y = x

print(x, id(x)) # 10 140710339589232
print(y, id(y)) # 10 140710339589232

x = 15
print(x, id(x)) # 15 140710339589392
print(y, id(y)) # 10 140710339589232

print('***************************************************************************************************************')

l1 = [1, 2, 3]
l2 = l1
print('1 - ', l1, id(l1)) # [1, 2, 3] 1757842186632
print('1 - ', l2, id(l2)) # [1, 2, 3] 1757842186632

l1.append(5)
print('2 - ', l1, id(l1)) # [1, 2, 3, 5] 1870760780104
print('2 - ', l2, id(l2)) # [1, 2, 3, 5] 1870760780104


l2 = l1.copy()
print('3 - ', l1, id(l1)) # [1, 2, 3, 5] 2825763889544
print('3 - ', l2, id(l2)) # [1, 2, 3, 5] 2825763930824

l2 = l1[:]
print('4 - ', l1, id(l1)) # [1, 2, 3, 5] 2825763889544
print('4 - ', l2, id(l2)) # [1, 2, 3, 5] 2825795086344

l1.append((5))
print('5 - ', l1, id(l1)) # [1, 2, 3, 5, 5] 2129239744904
print('5 - ', l2, id(l2)) # [1, 2, 3, 5] 2129270810760