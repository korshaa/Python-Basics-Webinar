user_list = list(input('Введите что угодно: '))
copy_list = user_list[::2]
index = 0
for i in user_list[1::2]:
    copy_list.insert(index, i)
    index += 2

print(copy_list)
