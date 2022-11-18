def WordsDeleting1(someText):
    someText = list(filter(lambda x: 'абв' not in x, someText.split()))
    return " ".join(someText)

# Teacher's function to save punctuation marks
def WordsDeleting2(someText):
    someText = someText.split()
    for i in range(len(someText)):
        if 'абв' in someText[i]:
            if not someText[i].isidentifier():
                someText[i] = someText[i][-1]
            else:
                someText[i] = ''
    return " ".join(someText)

print('Program will delete any words with "абв".')
text = str(input("Enter any text: "))
text = WordsDeleting1(text)
print(text)