file = open("note1.txt", "x")   # file တည်ဆောက်
file = open("note1.txt", "w")
file.write("Welcome from my Country")
file.close()
file = open("note1.txt", "r")
print(file.read())