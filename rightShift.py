# shiftRight.py
# Put your code here
print ("input a bit string: ")
bitString = input()
print ("This is your bit string: ", bitString)
print ("This program will now shift the bit string")


finalString = (bitString * 3)[len(bitString) - 1 : 2 * len(bitString) - 1]
print (finalString)