"""
File: encrypt.py
Project 4.3

Encypts a text file.  The inputs are the names of
the input file and the output file and the distance value.
The encrypted code is witten to a new file.
"""
#I'm getting the name of the file and converting it to a string (even though it is a string already)
#this is just for consistency in the code
print ("enter the name of the file you would like to encrypt")
fileName = input()
fileName = str(fileName)
#I'm going to open the file now in write mode to force python to create the file
print ("creating file")
sensitiveFile = open(fileName, 'w')
#Now I'm going to have python write some text into the file.
#This just ensures there is something for the program to encrypt.
print ("putting some text in the file")
sensitiveFile.write("bob is a builder")
#There is now a file with the text "bob is a builder in it"
#Now I am going to close the file. THis is just for consistency and to avoid any bugs.
print ("closing the file")
sensitiveFile.close
#now I am opening the file again, this time in read mode.
sensitiveFile = open(fileName,'r')
#Now I am importing the file as a string using the read method.
openFile = sensitiveFile.read()
#Now I am prompting for a distance value, getting the input and converting to an int.
print ("Enter the distance value: ")
distance = input()
distance = int(distance)
#declaring variable code, and converting it to a string
code = ""
code = str(code)
#This is the encryption code, I don't want to explain it all, we both know what it does.
for ch in openFile:
    ordValue = ord(ch)
    ordValue = int(ordValue)
    cipherValue = ordValue + distance
    if cipherValue > ord('z'):
#I do want to mention that the code on the next line keeps the characters within the ASCII values that
#correspond to lowercase letters
        cipherValue = ord('a') + distance - (ord('z') - ordValue + 1)
    code +=  chr(cipherValue)
#printing the resulting encrypted text
print ("This is the ecrypted text: ")
print(code)
#prompting for the name of the output file, assigning it to the variable and type conversion.
print("enter the save name of the new encrypted file")
encryptedFileName = input()
encryptedFileName = str(encryptedFileName)
#opening the file in write mode, which forces the creation of the output file.
#Then writing the encrypted text to the new file
encryptedFile = open(encryptedFileName,'w')
encryptedFile.write(code)
#closing all files to make sure the buffer is flushed and the files are saved.
sensitiveFile.close
encryptedFile.close