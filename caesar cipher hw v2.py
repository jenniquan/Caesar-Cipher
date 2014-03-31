from random import randrange

inputText = raw_input ("Enter message: ")
inputToAscii = map (ord, inputText)

cipherKeyABC = randrange (1, 26)
cipherKey123 = randrange (1, 10)

def addCipherKeyABC (y): return y + cipherKeyABC
asciiPlusKeyABC = map (addCipherKeyABC, inputToAscii)
def addCipherKey123 (y): return y + cipherKey123
asciiPlusKey123 = map (addCipherKey123, inputToAscii)
def addCipherKeyAll (y):
    if inputToAscii in range (97, 122):
        if asciiPlusKeyABC in range (97, 122):
            return y + cipherKeyABC
        elif asciiPlusKeyABC in range (123, 148):
            return asciiPlusKeyABC - y + 97
    elif inputToAscii in range (65, 90):
        if asciiPlusKeyABC in range (65, 90):
            return y + cipherKeyABC
        elif asciiPlusKeyABC in range (91, 116):
            return asciiPlusKeyABC - y + 65
    elif inputToAscii in range (48, 57):
        if asciiPlusKey123 in range (48, 57):
            return y + cipherKey123
        elif asciiPlusKey123 in range (58, 67):
            return asciiPlusKey123 - y + 48

cipheredAscii = map (addCipherKeyAll, inputToAscii)
cipheredText = map (chr, cipheredAscii)

print inputText
print inputToAscii
print cipherKeyABC
print cipherKey123
print cipheredAscii
print cipheredText
