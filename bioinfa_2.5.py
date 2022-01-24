x = [9, 8, 9, 4, 5, 8, 0, 1 ]
y = [7, 1]
dr = 0
result = []

if len(x) > len(y):
    max_arr = x
    min_arr = y
else:
    max_arr = y
    min_arr = x

for k in range (len(max_arr) - len(min_arr)):
    min_arr.append(0)

for i in range(len(max_arr)):
    result.append((min_arr[i] + max_arr[i] + dr) % 10)
    dr = (min_arr[i] + max_arr[i] + dr)//10

print(result)
