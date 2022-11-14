#it can store any datatypes in a single list
a = [54,28,20,3]

#print all list elements
print(a)

#particular index num like array index
print(a[2])

#list slice like strings
#output is given in new list 0 till 2
print(a[0:3])

#shortcuts (STL)
#changes in original list

l1=[43,5,2,666,56]
print("before sort",l1)
l1.sort()
print("SOrted is",l1)

#reverse list
l1.reverse()
print(l1)

#append (inserts at end)
l1.append(143)
print(l1)

#insert at index aage ke aage chale jayege
l1.insert(1,13)
print(l1)

#pop element of index
l1.pop(1) #delete element of index1
print(l1)

#remove element by searching in list
l1.remove(143) #delete 143 element
print(l1)

#count occurence of element
c=l1.count(666)
print(c)


# user input can be made using
#typecasting to int if needed
t1=int(input("enter :"))
t2=int(input("enter :"))
t3=int(input("enter :"))
t4= int(input("enter :"))

t=[t1,t2,t3,t4]
print(t)
#sum of all element of list
print(sum(t))
