number = int(input("Введите новый элемент рэйтинга: "))
numbers = [7, 7, 5, 3, 3, 2]

if number > numbers[0]:
    numbers.insert(0, number)
elif number < numbers[-1]:
    numbers.insert(len(numbers), number)
elif numbers.count(number) > 0:
    n = numbers.count(number)
    index = numbers.index(number) + n
    numbers.insert(index, number)
else:
    for i in range(len(numbers)):
        if number > numbers[i]:
            numbers.insert(i, number)
            break
print(numbers)
