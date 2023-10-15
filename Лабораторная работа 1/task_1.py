numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

missing_element = 4

sum_of_numbers = sum(numbers[:missing_element])+sum(numbers[missing_element+1:])
count_of_numbers = len(numbers)
average_of_numbers = sum_of_numbers / count_of_numbers
numbers[missing_element] = average_of_numbers

print("Измененный список:", numbers)
