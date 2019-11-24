limit = int(input())
numbers = int(input())
total = 0
count = 0
for i in range(numbers):
    total += int(input())
    if total <= limit:
        count += 1
print(count)
