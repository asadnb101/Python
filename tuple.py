t = (1 ,5 ,3 ,32)
print(t)

print(t[2])

#t[0]= 3
# tuple is immutable
#what is tupple?
# it is immutalbe that means the values cannot be changed.

u = t + (4,5,2,10)
print(u)

#slicing
v = u[2:6] + (6,8,34,87,65)
print(v)

a = ([1,2,3], [4,5,6], [7,8,9])
print(a[0][2])

a[0][0]= 100
print(a)
