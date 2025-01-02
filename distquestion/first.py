info = { "key" : "value", "name" : "ayush" , "learning" : "coding", "age" : 25 }

"""
print(info)
print(type(info))
print(info["name"])
info["name"] = "puja"
print(info)
"""

student = {"name" : "rahul kumar" , "subject" : {"phy" : 97, "che" : 98, "maths" : 99}}
print(student)
print(student["subject"])
print(student["subject"]["che"])
print(student.keys())
print(len(student))
print(student.values())
print(list(student.values()))
print(student.items())
print(list(student.items()))
pairs = list(student.items())
print(pairs[0])

# student.update({"city" : "bhagalpur"})
# print(student)

new_dict = {"city" : "delhi" }
student.update(new_dict)
print(student)
