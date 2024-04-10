def encode(code):
    output = ''
    for i in range(len(code)):
        if int(text[i]) + 3 > 10:
            output += str(int(code[i]) + 3 - 10)
        else:
            output += str(int(code[i]) + 3)
    return output

def decode(password):
    p=password
    final=""
    for letter in p:
        final+=str(int(letter)-3)
    return final

running = True
while running:
    print("Welcome to the Encoder Program!")
    print("1. Encode a number")
    print("2. Decode a number")
    print("3. Exit")
    i = input("Enter your choice: ")
    if i == "1":
        num = input("Enter an 8 digit number: ")
        print(encode(num))
    elif i == "2":
        pass
    elif i == "3":
        running = False
        print("Thank you for using the encoder program!")
    else:
        print("Invalid Input")
#spaghetti
