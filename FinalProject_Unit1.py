#Final Project Unit I
#This code will change the folder name

print("This is my Final Project - Console Application")
namechoice=input("Please input desired keywored to rename all files in subfolders or folder")


#Rename all files in subfolders of folder
import os

directoryName = "TEST FOLDER FOR FINAL PROJECT UNIT I"
filePath = ("C:\\\\Users\\bodhi\\SAVVYCODE\\DAPSupplementalCode\\TESTFOLDER1\\")
print(filePath)


files = os.listdir(filePath)
filePathWithSlash = filePath + "\\"
print(files)

for counter, filename in enumerate(os.listdir(filePath)):

    filenameWithPath = os.path.join(filePathWithSlash, "Test file I")

    split_file = os.path.splitext(filename)
    os.rename(filePath + filename, filePath + namechoice + str(counter) + split_file[1])

    print ("Successfully renamed.")

