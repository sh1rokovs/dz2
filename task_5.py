my_list = [7, 5, 3, 3, 2]
m = 8

# my_list = list(map(int, input('Введите числа через пробел').split()))

my_list_cp = my_list[:]
for k in range(len(my_list)):
    if my_list[k] < m:
        my_list.insert(k, m)
        break
    elif my_list[k] == m:
        my_list.insert(k+1, m)
        break
if len(my_list) == len(my_list_cp):
    my_list.append(m)
print(my_list)
