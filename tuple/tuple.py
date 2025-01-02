# set is ignore the dublicate value
collection = {1, 2, 3, 4, "Hello" , "World"}
print(collection)
print(type(collection))
print(len(collection))

collection = set()
collection.add(1)
collection.add(3)
collection.add(4)
collection.remove(1)
print(collection)

set1 = {1, 2, 3}
set2 = {2, 3, 4}

print(set1.union(set2))
print(set1.intersection(set2))
