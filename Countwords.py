#Program that counts how many times a word appears in the text.

#get file object reference to the file
file = open("C:\workspace\python\data.txt", "r")

#Read content of the file to string
data = file.read()

#count number of occurrences of the substring in the string
occurrences = data.count("python")

print('Number of occurrences of the word :', occurrences)

