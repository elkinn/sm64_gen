import pyperclip

genString = input("Enter text here:")
l = []
final = ""

for char in genString:
    if str.isalpha(char):
        temp = ":s64_" + char + ": "
        l.append(temp)
    else:
        l.append(char)

final = "".join(l)
pyperclip.copy(final)
print("SM64 text copied to clipboard")
print(final)