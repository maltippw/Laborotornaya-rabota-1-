numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
index_of_None = 4
sum_without_None = sum(numbers[:index_of_None] + numbers[index_of_None+1:])
count_of_None = len(numbers)
average_value = sum_without_None/count_of_None
numbers[index_of_None] = average_value
print("Измененный список:", numbers)
