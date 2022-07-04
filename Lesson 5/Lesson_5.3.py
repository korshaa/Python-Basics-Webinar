with open('text_3.txt', 'r', encoding='utf-8') as my_f:
    new_list = [i.split() for i in my_f]

dict_zp = {key: float(val) for key, val in new_list if float(val) < 20000.0}
print('Оклад менее 20 000 р.\n')
for key, val in dict_zp.items():
    print(f"{key}: {val}\n")

print(f"Средняя величина дохода сотрудников: {round(sum(dict_zp.values()) / len(dict_zp), 2)}")
