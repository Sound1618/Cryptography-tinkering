#Caesar Cypher Hacker
#This script was written to understand how Cyphers and Bruteforce Attacks work

#Output from Casear_cypher script goes here.
message = ''

# Same char list than in Caesar Cypher
Symbols = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZabcdefghijklmnñopqrstuvwxyz123456789 !?.'
key = 13

#Loop through every possible key combination:
for key in range(len(Symbols)):
    translated = ''
    for symbol in message:
        if symbol in Symbols:
            symbolIndex = Symbols.find(symbol)
            translatedIndex = symbolIndex - key

            #Wraparound
            if translatedIndex < 0:
                translatedIndex = translatedIndex + len(Symbols)

            #Append the decrypt symbol   
            translated = translated + Symbols[translatedIndex]

        else:
            translated = translated + symbol

# Will list all possible combinations            
print('Key #%s: %s' % (key, translated))