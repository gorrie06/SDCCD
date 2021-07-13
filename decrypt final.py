#I'm getting the name of the file and converting it to a string (even though it is a string already)
#this is just for consistency in the code
print ("enter the name of the file you would like to decrypt")
fileName = input()
fileName = str(fileName)
#now I am opening the file, this time in read mode.
sensitiveFile = open(fileName,'r')
#Now I am importing the file as a string using the read method.
openFile = sensitiveFile.read()
#Now I am prompting for a distance value, getting the input and converting to an int.
print ("Enter the distance value: ")
distance = input()
distance = int(distance)
#declaring variable plainText, and converting it to a string (again the type conversion isn't necessary but
#this is how I like to do it, it makes much much more sense) Python coding the way we are shown in the text is
# taking too many shortcuts for my taste. The code this way is much clearer.
plainText = ""
plainText = str(plainText)
#This is the encryption code, I don't want to explain it all, we both know what it does.
for ch in openFile:
    ordValue = ord(ch)
    ordValue = int(ordValue)
#this line is literally encryption in reverse.
    cipherValue = ordValue - distance
    if cipherValue > ord('z'):
#I do want to mention that the code on the next line keeps the characters within the ASCII values that
#correspond to lowercase letters
        cipherValue = ord('a') + distance - (ord('z') - ordValue + 1)
    plainText +=  chr(cipherValue)
#printing the resulting decrypted text
print ("This is the decrypted text: ")
print(plainText)
#prompting for the name of the output file, assigning it to the variable and type conversion.
print("enter the save name of the new decrypted file")
decryptedFileName = input()
decryptedFileName = str(decryptedFileName)
#opening the file in write mode, which forces the creation of the output file.
#Then writing the encrypted text to the new file
decryptedFileName = open(decryptedFileName,'w')
decryptedFileName.write(plainText)
#closing all files to make sure the buffer is flushed and the files are saved.
sensitiveFile.close
decryptedFileName.close