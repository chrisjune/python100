a = int(input())
b = int(input())

string = ''
total = 0
for i in range(a, b+1):
    string+= str(i)
for i in string:
    total += int(i)
print(string)
print(total)
