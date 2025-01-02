# WAP  to find the factorial of first n naturals. (using for) 

# using while loop
n = int(input("Enter the number :"))
fact = 1
i = 1
while i <= n:
    fact *= i
    i += 1
print("factorial" , fact)