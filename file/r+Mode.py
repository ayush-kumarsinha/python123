#open file for r+ mode. it is use for initaly read of the file
f = open("demo.txt" , "r+")
f.write("abc")
f.close()
