list_ = [3, -5, 7, 89, 56, 89, 89, 14, -90, 89, 89, 89]
max_number = max(list_)
count_max_number = list_.count(max_number)


for i in range(count_max_number):
  index = list_.index(max_number)
  del list_[index]

print(f'Второй по величине элемент в введенном массиве: {max(list_)}')

