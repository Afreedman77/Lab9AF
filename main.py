output = ''
running = True
while running:
    text = input("enter 8 digits: ")
    if text.isdigit() and len(text) == 8:
        for i in range(len(text)):
            if int(text[i])+3 > 10:
                output += str(int(text[i]) + 3-10)
            else:
                output += str(int(text[i])+3)
        running = False
print(output)
