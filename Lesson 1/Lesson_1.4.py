number = int(input("Enter a number: "))
max_num = 0
cut_num = 0

while number > 0:
    if number % 10 > max_num:
        max_num = number % 10
    number = number // 10

print(f"Max number: {max_num}")
