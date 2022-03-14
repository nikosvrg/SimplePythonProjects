def Initiate():
    phrase = raw_input("Insert you phrase Here:\t")
    CountParenthesis(phrase)
    

def CountParenthesis(phrase):
    PhraseLength = len(phrase)
    flag = "down"
    i = 0
    OpenningCounter = 0
    ClosingCounter = 0
    while i < PhraseLength:
        currentSymbol = phrase[i:i+1]
        if (ClosingCounter == OpenningCounter) and (currentSymbol == ")"):
            flag = "up"
        if currentSymbol == "(":
            OpenningCounter = OpenningCounter+1
        if currentSymbol == ")":
            ClosingCounter = ClosingCounter+1
        i = i+1
    if (flag == "up"):
        print("Expression is not Valid. Please try again.")
    else:
        if(OpenningCounter == ClosingCounter):
            print("\t Math Expression is Valid.")
        else:
            print("Expression is not Valid. Please try again.")
    answer = raw_input("Do you want to try another expression? (type y for yes)\t")
    if answer == "y":
        Initiate()

Initiate()