genString = input("Enter text here:")
l = []
final = ""

for char in genString:
    if str.isalpha(char):
        temp = ":sm64_" + char + ": "
        l.append(temp)
    else:
        l.append(char + " ")

final = "".join(l)
print("SM64 text printed below:")
print(final)