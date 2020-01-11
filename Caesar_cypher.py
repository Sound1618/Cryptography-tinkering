#Basic script implementing Caesar cypher
import paperclip

message = 'This is my encrypted message'

#Simetric Key
key = 13

#This mode needs to be set manually to 'encrypt' or 'decrypt'. Other input will fail.
mode = 'encrypt'

Symbols = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZabcdefghijklmnñopqrstuvwxyz123456789 !?.'

#Pass the stored string
translated = ''

for symbol in message:
    if symbol in Symbols:
        symbolIndex = Symbols.find(symbol)

        #encryption/decription process
        if mode =='encrypt':
            translatedIndex = symbolIndex + key
        elif mode =='decrypt':
            translatedIndex = symbolIndex - key
        
        if translatedIndex >= len(Symbols):
            translatedIndex = translatedIndex - len(Symbols)
        elif translatedIndex < 0:
            translatedIndex = translatedIndex + len(Symbols)
        
        translated = translated + Symbols[translatedIndex]
    else:
        #Append symbol without modification
        translated = translated + symbol

#Output
print(translated)
paperclip.copy(translated)


