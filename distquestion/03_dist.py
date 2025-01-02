#WAP to enter of 3 subject from the user and store them in a dictionary. start withh an empty dictionary and add one by one . Use subject name as key and marks as value

marks = {}
x = int(input("Enter pyh : "))
marks.update({"phy" : x})

x = int(input("Enter math : "))
marks.update({"math" : x})

x = int(input("Enter che : "))
marks.update({"che" : x})

print(marks)

