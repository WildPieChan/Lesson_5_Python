def Coding(data):
    count = 1
    result = ''
    for i in range(len(data) - 1):
        if data[i] == data[i + 1]:
            count += 1
        else:
            result = result + str(count) + data[i]
            count = 1
    if count > 1 or (data[len(data) - 2] != data[-1]):
        result = result + str(count) + data[-1]
    return result

def Decoding(data):
    number = ''
    result = ''
    for i in range(len(data)):
        if not data[i].isalpha():
            number += data[i]
        else:
            result = result + data[i] * int(number)
            number = ''
    return result


text = input("Enter a text for coding: ")
print(f"Coding text: {Coding(text)}")
print(f"Decoding text: {Decoding(Coding(text))}")