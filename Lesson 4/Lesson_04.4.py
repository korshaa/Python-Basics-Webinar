sour_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
rez_list = [num for num in sour_list if sour_list.count(num) == 1]
print(rez_list)
