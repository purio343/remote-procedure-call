import math

def floor(num):
    return math.floor(num)

def nroot(num_list):
    n, x = num_list
    return math.pow(x, 1/n)

def reverse(string):
    string_reversed = string[::-1]
    return string_reversed

def validAnagram(arr):
    string1, string2 = arr
    string1_list = sorted(string1)
    string1_sorted = ''.join(string1_list)
    string2_list = sorted(string2)
    string2_sorted = ''.join(string2_list)
    return string1_sorted == string2_sorted

def sort(arr):
    return sorted(arr)