number = 1534351
n = 0


for i in range(len(str(number))//2):
  if str(number)[i] == str(number)[-(i+1)]:
    n += 1
if n == len(str(number))//2:
  print(f'Число {number} палиндром.')
else:
  print(f'Число {number} не является палиндромом.')
