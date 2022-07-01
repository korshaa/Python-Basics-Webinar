def div_num(num_1, num_2):
    result = num_1 / num_2
    print(f"Result: {int(result)}") if num_1 % num_2 == 0 else print(f"Result: {result}")


try:
    div_num(int(input("Enter the first number(int): ")), int(input("Enter the second number(int): ")))
except (ZeroDivisionError, ValueError) as err:
    print(err)
