arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# arr = list(map(int, input('Введите некоторое количество целых чисел через пробел: ').split()))
print(arr)
arr_cp = arr[:]
k = 0

if len(arr) % 2 != 0:
    k = arr.pop(-1)
    arr[::2], arr[1::2] = arr[1::2], arr[::2]
    arr.append(k)
else:
    arr[::2], arr[1::2] = arr[1::2], arr[::2]

print(arr)
print(k)
