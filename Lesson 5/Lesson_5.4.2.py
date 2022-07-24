# еще один вариант который появился при решение других задач

with open('text_4.txt', 'r', encoding='utf-8') as my_f, \
        open('text_4.1.txt', 'w', encoding='utf-8') as my_f1:
    dic_num = {1: 'Один', 2: 'Два', 3: 'Три', 4: 'Четыре'}
    new_list = [i.strip().split('-') for i in my_f]
    print(new_list)

    for i in new_list:
        i[0] = dic_num.get(int(i[1]))
        my_f1.write(f'{" - ".join(i)}\n')
