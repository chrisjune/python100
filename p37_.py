names = input().split()
idx = 0
for i in range(len(names)-1):
    if names.count(names[i]) < names.count(names[i+1]):
        idx = i
print(names[i], names.count(names[i]))

