def swapList(newList):
    size = len(newList)
    temp = newList[0]
    newList[0] = newList[size -1]
    newList[size -1] = temp
    
    return newList
newList = [12, 89, 78, 5265, 12549]
print(swapList(newList))