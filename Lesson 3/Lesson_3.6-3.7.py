def int_func(my_str):
    new_list = []
    for i in my_str.split():
        if i.islower():
            if i.isascii():
                new_list.append(i)

    return (' '.join(new_list)).title()


print(int_func("nice авп ъghj jапAро hjjпаро вапрghgh cool ZUUss"))
