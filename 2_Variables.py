#no need to declare int float vagera direct use
a="pikachu"

#multi line string
f='''altaf
is
pikachu'''

b=28
c=34.45
d=False
e=None

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(type(1 + 3j))              # Complex no
print(type([1, 2, 3]))           # List like arrays
print(type({'name':'Asabeneh'})) # Dictionary like objects
print(type({9.8, 3.14, 2.7}))    # Set
print(type((9.8, 3.14, 2.7)))    # Tuple

#typeof datatype find
print(type(a))
print(type(b))

#typecasting
a="345"
a=int(a)
b=str(3) #typecasting it to '3'

#a=str(a) #typecasting str from int
print(a+5)
