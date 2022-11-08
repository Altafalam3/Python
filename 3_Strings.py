# a="altaf"
# a  l  t  a  f
# 0  1  2  3  4
# -5 -4 -3 -2 -1
#immutable strings
#Char is a 1 size string bcz py doesn't has char datatype
greet ="heyy "
name="pikachu"

#concat
c=greet+name
print(c)
print(c[10])

#String and number cannot concat in py

#[1:] 1 to end
#[:3] start0 to 2
#slice from 0 to 3
print(name[0:4])

#slice with skip
#print skip 1st then print 3rd
d=name[1:4:2]
print(d)

#length
print(len(name))

f=name.endswith("hu")

#character count
f=name.count("c")

f=name.find("ka") #return first occur index
f=name.replace("chu","altaf")

print(name.capitalize()) #1st letter capital only
