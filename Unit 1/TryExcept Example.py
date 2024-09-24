try:
    fileName = input("File name: ")
    file = open(fileName, "r")
except:
    print("File not found.")
