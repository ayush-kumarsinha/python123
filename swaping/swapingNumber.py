# Swap the first and last element

def swap(element):
    element[0] , element[-1] = element[-1] , element[0]
    return element
element = [78, 25, 5986, 856, 54] 
print(swap(element))