list1 = [8, 19, 148, 4]
list2 = [9, 1, 33, 83]
full_list = []

for i in list1:
    for x in list2:
        full_list.append(i * x)

print(full_list)


list1 = [8, 19, 148, 4]
list2 = [9, 1, 33, 83]
list3 = []

for i in list1:
    for j in list2:
        mult = i * j
        list3.append(i * j)

print(list3)
