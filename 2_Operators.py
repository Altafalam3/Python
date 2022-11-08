#Multiple variable declare same line
a,b=4,3

print("add is:",a+b)
print("mult is:",a*b)
print("div is:",a/b) #smart divide
print("power is:",a**b)
print("floor division is:",a//b) # bad division

# remaining same == < > += -= so on
bo1=True
bo2=False

#instead of && || ! use english word
print("and use:",(bo1 and bo2))
print("or use:",(bo1 or bo2))
print("not use:",(not bo2))

#tuple ka values variables mai
# fruits = ["apple", "banana", "cherry"]
# x, y, z = fruits

# Identity Operators
#used to compare the objects, not if they are equal ==
#but if they are actually same object, with same memory location

y=34
x=y #(clone kr dega and same memory location)

Print(x is y)
print(x is not y)
