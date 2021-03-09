# Explain your work
'''
I created two lists and then merged them.
For clarity, I also used the sort method to sort the merged list.
Lastly, I used a for loop to print the type of each element in the final list.
'''

# Answer to Question 1
even_num = list(range(0, 10, 2))
odd_num = list(range(1, 10, 2))
# print(even_num)
# print(odd_num)

merged_nums = even_num + odd_num
merged_nums.sort()
# print(merged)

for num in merged_nums:
	print("Type of {num} is {type_of_num}.".format(num=num, type_of_num=type(num)))
