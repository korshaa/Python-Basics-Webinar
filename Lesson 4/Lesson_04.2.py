source_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list = [i for i in source_list[1:] if i > source_list[source_list.index(i)-1]]
print(new_list)
