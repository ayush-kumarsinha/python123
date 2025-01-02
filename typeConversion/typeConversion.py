"""
Type conversion
----> two type of type conversion
1. conversion(automatically)
2. Casting(manual) """

a = 2 
b = 4.0255
sum = a + b # 2.0000 + 4.0255
print(sum)


a = "2"  # a = int("2")
b = 4.25
a = int(a)
print(a + b)
print(type(a))