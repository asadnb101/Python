import numpy as np

ls = [1, 4, 9, 16, 25,36]

a = np.arange(6)
print(a)
print(type(a))

sq = np.array(ls)
print(sq, type(sq))

aa = np.array([[11,2,30,4,5],[5,6,7,8,9],[10,11,12,13,14]])
print(aa , type(aa))
print(sq[2])
print(aa[1][1])

aa.sort()
print(aa)

x = np.array([1,2,3])
y = np.array([4,5,6])

z = np.concatenate((x,y))
print(z)

print(aa.ndim)
print(aa.size)

newSq = sq.reshape(3,2)
print(newSq)
print(sq)