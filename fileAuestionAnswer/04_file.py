# WAF to find in which line of the file does the word "learning" occur first. print -1 if word not found
def check_for_word():
    word = "learning"
    with open("practic.txt" , "r") as f:
        data = f.read()
        
        if(word in data):
            print("Found")
        else:
            print("not found")