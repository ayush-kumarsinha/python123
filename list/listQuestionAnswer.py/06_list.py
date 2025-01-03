#Search for a number X in this tuple using loop.[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
x = 49
idx = 0
for ele in nums:
    if(ele == x):
        print("number found at idx" , idx)
        break
    idx += 1