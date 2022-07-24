with open('text_6.txt', 'r', encoding='utf-8') as my_f:
    new_list = [i.strip().split(":") for i in my_f]
    dict_less = {key: sum([int(n) for i in val.split() for n in i.split("(") if n.isdigit()]) for key, val in new_list}
    print(dict_less)
