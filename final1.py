def Initiate():
    phrase = raw_input("Insert your Phrase here \t -> ")
    CutExclamation(phrase)

def CutExclamation(phrase):
    i = 0
    length = len(phrase)
    while (i != length):
        currentSymbol = phrase[i:i+1]
        NextSymbol = phrase[i+1:i+2]
        if ((currentSymbol == "!") and ( NextSymbol != "")):
            a = phrase[:i]
            b = phrase[i+1:]
            phrase = a + b
        i = i+1
    print(phrase)


Initiate()