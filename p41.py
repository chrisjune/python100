number = int(input())
result = None
if number == 1:
    result = 'NOT PRIME'
if number == 2:
    result = 'PRIME'

for i in range(2, number//2+1):
    if number % i == 0:
        result = 'NOT PRIME'
        break
if not result:
    result = 'PRIME'
print(result)

