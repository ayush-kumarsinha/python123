d = {} # this is empty dictionary
marks = {
    "harry": 100,
    "ayush": 56,
    "rohan": 23
}

print(marks, type(marks))

print((marks.items()))
print((marks.keys()))
print((marks.values()))


marks.update({"harry": 99, "ranuka": 3454})
print(marks)