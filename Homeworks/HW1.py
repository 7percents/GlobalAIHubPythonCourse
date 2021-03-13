# Explain your work
'''
I created two lists and then merged them. For clarity, I also used the sort method on the merged list so that numbers had an order.
Using a list comprehension, I multiplied all values in the list by 2.
Lastly, I used a for loop to print the type of each element in the final list.
'''

# Homework 1
odd_num = list(range(1, 10, 2))
even_num = list(range(0, 10, 2))

merged_nums = odd_num + even_num
merged_nums.sort()

merged_nums_multiplied = [num * 2 for num in merged_nums] # multiplied all values by 2

for num in merged_nums_multiplied:
	print("Type of {num} is {type_of_num}.".format(num=num, type_of_num=type(num)))