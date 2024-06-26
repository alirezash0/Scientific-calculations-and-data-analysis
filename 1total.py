# -*- coding: utf-8 -*-
"""2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1tFEtGY1D_UzLV0ECv41okgxvG2-u-Ru_

Question 1:
You are given a list of words as strings. Write a Python function that finds the longest word in the list. But you should only consider words that contain the letter 'a' in them. If there are multiple words that meet this criteria and have the same length, return the word that appears first in the list.
"""

def longest_word(my_word):
    longest_word = ""

    for word in my_word:
        if 'a' in word and len(word) > len(longest_word):
            longest_word = word

    if longest_word:
        return longest_word
    else:
        return "No words found"

word_list = [""]
result = longest_word(word_list)
print(result)

#Test1
word_list = ["banana", "apple", "cherry", "grape", "kiwi", "date"]
result = longest_word(word_list)
print(result)

#Test2
word_list = ["pear", "orange", "apricot", "blueberry", "apple"]
result = longest_word(word_list)
print(result)

#Test3
word_list = ["apple", "banana", "cherry", "date", "apricot"]
result = longest_word(word_list)
print(result)

#Test4
word_list = ["blueberry", "cherry", "kiwi", "melon"]
result = longest_word(word_list)
print(result)

"""Question 2:
Write a Python program that takes a string as input from the user and checks if it is a palindrome. A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward, ignoring spaces, punctuation, and capitalization. Your program should return True if the input string is a palindrome and False otherwise.
"""

def palindrome(s):
    s = ''.join(s.split())
    s = s.lower()
    s = s.translate(str.maketrans('', '', string.punctuation))

    left, right = 0, len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

input_user = input("input:")

if palindrome(input_user):
    print("true")
else:
    print("false")

"""Question 3:
You are given a list of integers. Write a Python program to find and print the sum of all even numbers in the list. Additionally, calculate and print the product of all odd numbers in the list. Answer with -1 whenever there is no even(odd) number.
"""

def sum_and_product(numbers):
    sum_even = 0
    product_odd = 1
    even = False
    odd = False

    for num in numbers:
        if num % 2 == 0:
            sum_even += num
            even = True
        else:
            product_odd *= num
            odd = True

    if even:
        print(f"Sum of even numbers: { sum_even}")
    else:
        print("Sum of even numbers: -1")

    if odd:
        print(f"Product of odd numbers: {product_odd}")
    else:
        print("Product of even numbers: -1")

numbers_list = [1, 2, 3, 4, 5, 6]
sum_and_product(numbers_list)

"""Question 4:
Write a Python function to reverse a list using a for loop.
"""

def reverse(list):
    reverse = []
    for word_number in list:
        reverse.insert(0, word_number)
    return reverse

list = [1, 3, 5, 7, 9]
reverse = reverse(list)
print(reverse)

"""Question 5:
Write a Python program to find the index of a target element in a sorted list of integers (Binary search algorithm). Your program should return the index of the target or -1 if the target is not present.
Hint:
1. Start with the entire sorted list.
2. Compare the target with the middle element of the list.
3. If the middle element is equal to the target, you've found it.
4. If the middle element is greater than the target, repeat the process on the left half of the list.
5. If the middle element is less than the target, repeat the process on the right half of the list.
6. Continue this process, halving the search space with each step, until you find the target or determine it's not in the list.
"""

def binary_search(sorted_list, target):
    left, right = 0, len(sorted_list) - 1

    while left <= right:
        mid = (left + right) // 2

        if sorted_list[mid] == target:
            return mid
        elif sorted_list[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

sorted_list = [1, 3, 5, 7, 9, 11, 13, 15, 17]
target = 8

index = binary_search(sorted_list, target)

if index != -1:
    print(f"{index}")
else:
    print("-1")