numbers = []
sum = 0
while sum <= 100:
    num = float(input("Please enter a number:"))
    numbers.append(num)
    sum += num

print("Sum of entered numbers is greater than 100. The numbers entered were: ", numbers)
