#list is made using [] while tuple using ()
a=(1,5,3,34,2)

print(a[1])
#tuples vale cannot be updated immutable
#eg a[1]=34 ERROR

t1=() #empty tuple
t1=(2,) #single element tuple(, necessary here)

print(a)

#element index
print(a.index(34))
print(a.count(34))