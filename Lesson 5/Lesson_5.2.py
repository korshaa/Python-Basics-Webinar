with open('text_4.txt', 'r', encoding='utf-8') as my_f:
    my_list = [i.strip() for i in my_f]

print(f"Кол-во строк - {len(my_list)}")
for i in range(len(my_list)):
    y = 0
    for n in my_list[i]:
        if n == " ":
            y += 1
    print(f'Слов в строке {i + 1} - {y + 1} шт.')

# Второе решение, догодался когда делал 4 задание

with open('text_4.txt', 'r', encoding='utf-8') as my_f:
    new_list = [i.split() for i in my_f]
print(f"Кол-во строк - {len(new_list)}")
for e, i in enumerate(new_list, 1):
    print(f'Слов в строке {e} - {len(i)} шт.')
