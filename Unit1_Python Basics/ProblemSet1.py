# Problem 1
# Assume s is a string of lower case characters.

# Write a program that counts up the number of vowels contained in the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if s = 'azcbobobegghakl', your program should print:

# Number of vowels: 5

# problem 1
# s = 'azcbobobegghakl'
count = 0
for i in s:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        count = count + 1
print("Number of vowerls:",count)


# Problem 2
# Assume s is a string of lower case characters.

# Write a program that prints the number of times the string 'bob' occurs in s. For example, if s = 'azcbobobegghakl', then your program should print

# Number of times bob occurs is: 2

# problem 2
# s = 'azcbobobegghakl'
count = 0
for i in range(len(s)-2):
    temp = s[i:i+3]
    if temp == 'bob':
        count = count + 1
print("Number of times bob occurs is:",count)


# Problem 3
# Assume s is a string of lower case characters.

# Write a program that prints the longest substring of s in which the letters occur in alphabetical order. For example, if s = 'azcbobobegghakl', then your program should print

# Longest substring in alphabetical order is: beggh
# In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print

# Longest substring in alphabetical order is: abc
# Note: This problem may be challenging. We encourage you to work smart. If you've spent more than a few hours on this problem, 
# we suggest that you move on to a different part of the course. If you have time, come back to this problem after you've had a break and cleared your head.

# problem 3
# s = 'abcbcd'
count = 0
sMax = ''
temp = s[0]
for i in range(1,len(s)):
    if ord(s[i]) >= ord(s[i-1]):
        temp = temp + s[i] 
        if len(temp) == len(s):
            sMax = temp
        # 最后一次的判断
        if i == len(s)-1:
            if count < len(temp):
                count = len(temp)
                sMax = temp
    else:
        if count < len(temp):
            count = len(temp)
            sMax = temp
        # 只要进到else分支，就应该初始化temp
        temp = s[i]

print("Longest substring in alphabetical order is:", sMax)

