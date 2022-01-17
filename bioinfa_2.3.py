list_ = [3, -5, 7, 89, 56, 89, 89, 14, -90, 89, 89, 89]
max_number = max(list_)
count_max_number = list_.count(max_number)


for i in range(count_max_number):
  index = list_.index(max_number)
  del list_[index]

max_number_2 = max(list_)
count_max_number_2 = list_.count(max_number_2)

for i in range(count_max_number_2):
  index_2 = list_.index(max_number_2)
  del list_[index_2]

print(f'Третий по величине элемент в введенном массиве: {max(list_)}')
