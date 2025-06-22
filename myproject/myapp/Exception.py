try:
    file = open("note1.txt", "r")
except IOError:
    print("File Not Found")
else:
    print(file.read())