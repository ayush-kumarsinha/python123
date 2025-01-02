# Write a recursive function to print all elements in a list. [Hint : use list and index as parameters]

def print_list(list, idx=0):
    if(idx == len(list)):
        return
    print(list[idx])
    print_list(list, idx+1)
fruts = ["mango", "litchi", "apple", "banana"]
print_list(fruts)