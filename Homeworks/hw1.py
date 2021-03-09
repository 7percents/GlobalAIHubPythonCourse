# Explain your work
'''
I created two lists and then merged them. For clarity, I also used the sort method to sort the merged list.
Using a list comprehension, I multiplied all values in the list by 2.
Lastly, I used a for loop to print the type of each element in the final list.
'''
# Answer to Question 1
even_num = list(range(0, 10, 2))
odd_num = list(range(1, 10, 2))
# print(even_num)
# print(odd_num)

merged_nums = even_num + odd_num
merged_nums.sort()
# print(merged_nums)

merged_nums_multiplied = [num * 2 for num in merged_nums]
# print(merged_nums_multiplied)

for num in merged_nums_multiplied:
	print("Type of {num} is {type_of_num}.".format(num=num, type_of_num=type(num)))