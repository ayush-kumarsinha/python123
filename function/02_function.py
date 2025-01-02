# WAF to print the elements of a list in a string in a single line. (list in the parameter)
heroes =  ["salman", "ritik", "katrina", "caption america", "saktiman"] 
cities = ["delhi", "gurgao", "bhagalpur", "munger", "salem", 'channi']
def print_list(list):
    for item in list:
        print(item, end=" ")
print_list(heroes)  
print_list(cities)