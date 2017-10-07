"""
@author: azubiolo (alexis.zubiolo@gmail.com)
"""

# Factorial of a given integer.
def fact(x):
    if x == 0:
        return 1
    return x * fact(x - 1)

# Maximum of a list of non-negative integers. Please do not use the built-in function 'max'.
def maximum_value(l):
    max_value = 0
    for x in l:
        if x > max_value:
            max_value = x
    return max_value
    
# Average value of a list. Try not to use the functions 'len' or 'sum'.
def average_value(l):
    sum_elements = 0.0 # try with 0 instead of 0.0 
    n_elements = 0
    for x in l:
        sum_elements += x
        n_elements += 1
    return sum_elements/n_elements

# Write a function filter(a, b) which finds all numbers between integers a and b (both 
# included) which are divisible by 7 but not by 5.
def filter(a, b):
    result = []
    for i in range(a, b+1):
        if (i%7 == 0) and (i%5 != 0): # if the number is divisible by 7 but not by 5 then add it.
            result.append(i)
        # else don't do anything
    return result
    
# Write a function that takes a value and a list of values and returns True if the value is
# in the list, False otherwise.
def is_member(a, l):
    result = False
    for x in l:
        if a == x:
            result = True
    return result
    
# Write a function reverse(word) that reverses a word. For example, reverse("boat")
# should return "taob"
def reverse(word):
    reversed_word = "" # 
    for letter in word:
        reversed_word = letter + reversed_word # + for strings is a concatenation
    return reversed_word
    
# Write a function is_palindrome(word) that recognizes palindromes (i.e. words 
# that look the same written backwards). For example, is_palindrome("radar") 
# should return True. is_palindrome("boat") should return False
def is_palindrome(word):
    return reverse(word) == word

# Write a function overlapping(list1, list2) that takes 2 lists and returns True if they 
# have at least one common element.
def overlapping(list1, list2):
    result = False
    for x1 in list1:
        if is_member(x1, list2):
            result = True
    return result

# Write a function char_freq() that takes a string and builds a frequency 
# listing of the characters contained in it. Represent the frequency listing 
# as a dictionary.
def char_freq(word):
    result = dict()
    for letter in word:
        if letter in result:
            result[letter] += 1
        else:
            result[letter] = 1
    return result
    
# Quick sort. Description of the algorithm here: https://en.wikipedia.org/wiki/Quicksort
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) / 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)