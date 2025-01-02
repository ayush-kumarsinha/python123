#open file for a+
f = open("demo.txt" , "a+")
print(f.read())
f.write("abc")
f.close()