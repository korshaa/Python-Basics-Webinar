# user_list = list(input('Введите что угодно: '))
user_list = [1, 2, 3, 4, 5, 6, 7]
for i in range(1, len(user_list), 2):
    user_list[i-1], user_list[i] = user_list[i], user_list[i-1]
print(user_list)