#WAP to check if a list contains a palidrome of elements. 
list1 = [1, 2, 1]
copy_list1 = list1.copy()
copy_list1.reverse()

if(copy_list1 == list1):
    print("palidrome")
else:
    print("Not palidrome")
