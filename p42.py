days_of_month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
month = int(input())
day = int(input())
if month > 12 or day > 31:
    raise Exception('Input is not allowed')

days = 3 - 1
for i in range(month - 1):
    days += days_of_month[i]
days += day

left = days % 7
if left == 0:
    print("SUN")
if left == 1:
    print("MON")
if left == 2:
    print("TUE")
if left == 3:
    print("WED")
if left == 4:
    print("THU")
if left == 5:
    print("FRI")
if left == 6:
    print("SAT")
