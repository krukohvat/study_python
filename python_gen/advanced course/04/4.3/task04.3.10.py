'''my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
sum = 0
for i in range(len(my_list)):
    for j in range(len(my_list[i])):
        sum += my_list[i][j]
print(sum)'''

my_list = [[1, 9, 8, 7, 4], [7, 3, 4], [2, 1]]

total = 0
for row in my_list:      # в один цикл
    total += sum(row)
print(total)