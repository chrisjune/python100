text = input()
result = ""
for i in text:
    if 'a' <= i and i <= 'z':
        result += i.upper()
    else:
        result += i.lower()
print(result)
