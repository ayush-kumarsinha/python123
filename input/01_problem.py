"""
name = input("Enter your name : ")

print("welcome : ", name)
"""
"""
val = input("Enter some value: ")
print(type(val), val)  """
# it is return string so this reason apply Type Casting

    
"""
val = int(input("Enter some value: "))
print(type(val), val)  """


name  = input("Enter your name: ")
print(name)
age = int(input("Enter your age: "))
marks = float(input("Enter your marks: "))

print("Welcome: ", name)
print(age)
print(marks)

food = input("food : ")
eat = "Yes" if food == "cake" else "no"
print(eat) 

food = input("food : ")
print("sweet") if food == "cake" or food == "jalebi" else print("not sweet")


age = int(input("age : "))
vote = ("yes" , "no") [age <= 18]
print(vote)

sal = float(input("salary : "))
tax = sal*(0.1, 0.2) [sal >= 5000]
print(tax)

