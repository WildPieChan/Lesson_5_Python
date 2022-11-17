def WordsDeleting(someText):
    someText = list(filter(lambda x: 'абв' not in x, someText.split()))
    return " ".join(someText)

print('Program will delete any words with "абв".')
text = str(input("Enter any text: "))
text = WordsDeleting(text)
print(text)