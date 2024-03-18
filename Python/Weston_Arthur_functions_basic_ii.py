# 1.Countdown - Create a function that accepts a number as an input. Return a new list that counts down by one, from the number (as the 0th element) down to 0 (as the last element).
# Example: countdown(5) should return [5,4,3,2,1,0]
# def countdown(n, nums=[]):
#     nums = nums.copy()
#     if n >= 0:
#         nums.append(n)
#         return countdown(n-1, nums)
#     else:
#         return nums
# result = countdown(5)
# print(result)


# 2.Print and Return - Create a function that will receive a list with two numbers. Print the first value and return the second.
# Example: print_and_return([1,2]) should print 1 and return 2

# def printAndReturn(some_list):
#     print(some_list[0])
#     return some_list[1]

# x=printAndReturn([1,2])
# print(x)
    
    

# 3.First Plus Length - Create a function that accepts a list and returns the sum of the first value in the list plus the list's length.
# Example: first_plus_length([1,2,3,4,5]) should return 6 (first value: 1 + length: 5)
# def first_plus_length ():
    
# def firstPlusLength(list):
#     sum = list[0] + len(list)
#     print(sum)
# firstPlusLength([1,2,3,4,5])
    
    

# 4.Values Greater than Second - Write a function that accepts a list and creates a new list containing only the values from the original list that are greater than its 2nd value. Print how many values this is and then return the new list. If the list has less than 2 elements, have the function return False
# Example: values_greater_than_second([5,2,3,2,1,4]) should print 3 and return [5,3,4]
# Example: values_greater_than_second([3]) should return False
# def val_second ():
    
# def greaterThanSecond(list):
#     counter = 0
#     new_list = []
#     for i in range(len(list)):
#         if len(list) < 2:
#             return False
#         if list[i] > list[2]:
#             counter += 1
#         if list[i] > list[2]:
#             new_list.append(list[i])
#     print(counter)
#     return new_list

# print(greaterThanSecond([1,2,3,4,5]))
# print(greaterThanSecond([1]))
    

# 5.This Length, That Value - Write a function that accepts two integers as parameters: size and value. The function should create and return a list whose length is equal to the given size, and whose values are all the given value.
# Example: length_and_value(4,7) should return [7,7,7,7]
# Example: length_and_value(6,2) should return [2,2,2,2,2,2]
# def length_value ():



