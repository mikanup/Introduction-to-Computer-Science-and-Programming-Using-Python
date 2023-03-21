# Problem 3
# 10.0/10.0 points (graded)
# Answer the following question without running the code. The procedure isMyNumber is used to hide a secret number (integer). It takes an integer x as a parameter and compares it to the secret number. It returns:

# -1 if the parameter x is less than the secret number

# 0 if the parameter x is correct

# 1 if the parameter x is greater than the secret number

# The following procedure, jumpAndBackPedal, attempts to guess a secret number. The only way it can interact with the secret number is through the isMyNumber procedure explained above.

# def jumpAndBackpedal(isMyNumber):
#     '''
#     isMyNumber: Procedure that hides a secret number. 
#      It takes as a parameter one number and returns:
#      *  -1 if the number is less than the secret number
#      *  0 if the number is equal to the secret number
#      *  1 if the number is greater than the secret number
 
#     returns: integer, the secret number
#     ''' 
#     guess = 1
#     if isMyNumber(guess) == 1:
#         return guess
#     foundNumber = False
#     while not foundNumber:
#         sign = isMyNumber(guess)
#         if sign == -1:
#             guess *= 2
#         else:
#             guess -= 1
#     return guess
# Unfortunately, the implementation given does not correctly return the secret number. Please fix the errors in the code such that jumpAndBackpedal correctly returns the secret number.
def jumpAndBackpedal(isMyNumber):
    '''
    isMyNumber: Procedure that hides a secret number. 
     It takes as a parameter one number and returns:
     *  -1 if the number is less than the secret number
     *  0 if the number is equal to the secret number
     *  1 if the number is greater than the secret number
 
    returns: integer, the secret number
    ''' 
    guess = 1
    if isMyNumber(guess) == 0:
        return guess
    foundNumber = False
    while not foundNumber:
        sign = isMyNumber(guess)
        if sign == 0:
            foundNumber = True
        elif sign == -1:
            guess *= 2
        else:
            guess -= 1
    return guess
    
def isMyNumber(x):
    secretNum = 100
    if x == secretNum:
        return 0
    elif x < secretNum:
        return -1
    else:
        return 1


# Problem 4
# 15.0/15.0 points (graded)
# Write a Python function that returns the sublist of strings in aList that contain fewer than 4 characters. For example, if aList = ["apple", "cat", "dog", "banana"], your function should return: ["cat", "dog"]

# This function takes in a list of strings and returns a list of strings. Your function should not modify aList.

# def lessThan4(aList):
#     '''
#     aList: a list of strings
#     '''
#     # Your code here

# Paste your function here
def lessThan4(aList):
    '''
    aList: a list of strings
    '''
    targetList = []
    for i in aList:
        if len(i) < 4:
            targetList.append(i)
    return targetList


# Problem 5
# 20.0/20.0 points (graded)
# Write a function called dict_invert that takes in a dictionary with immutable values and returns the inverse of the dictionary. The inverse of a dictionary d is another dictionary whose keys are the unique dictionary values in d. The value for a key in the inverse dictionary is a sorted list of all keys in d that have the same value in d.

# Here are some examples:

# If d = {1:10, 2:20, 3:30} then dict_invert(d) returns {10: [1], 20: [2], 30: [3]}
# If d = {1:10, 2:20, 3:30, 4:30} then dict_invert(d) returns {10: [1], 20: [2], 30: [3, 4]}
# If d = {4:True, 2:True, 0:True} then dict_invert(d) returns {True: [0, 2, 4]}
# def dict_invert(d):
#     '''
#     d: dict
#     Returns an inverted dictionary according to the instructions above
#     '''
#     # Your code here
# Paste your entire function, including the definition, in the box below. Do not leave any debugging print statements.

def dict_invert(d):
    '''
    d: dict
    Returns an inverted dictionary according to the instructions above
    '''
    # 定义字典，value是没有排序好的
    targetD = {}
    # 定义字典的value，是list类型的
    # 临时用的
    valueList = []

    # 循环input字典
    for key,value in d.items():
        # 每次循环开始初始化
        # 塞字典的value
        tempList = []

        # 先判断原字典的value在不在对象字典的key种出现过
        if value in targetD.keys():
            # 如果出现过，先去取出对象弟字典的value
            valueList = targetD[value]
            # 然后将值塞进去
            valueList.append(key)
        else:
            # 如果没出现过，直接塞到valuelist里
            tempList.append(key)
            # 然后把list给这个对象字典
            targetD[value] = tempList
    # 定义最后要输出的对象字典
    # value是排序好的
    answerD = {}
    # 循环字典
    for keyOfT,valueOfT in targetD.items():
        # 如果list value的值超过一个
        if len(valueOfT) > 1:
            # 开始排序
            valueOfT.sort()
        # 每次都将排好序的value塞进对象字典
        answerD[keyOfT] = valueOfT

    return answerD


# Problem 6
# 20.0/20.0 points (graded)
# Write a recursive Python function, given a non-negative integer N, to calculate and return the sum of its digits.

# Hint: Mod (%) by 10 gives you the rightmost digit (126 % 10 is 6), while doing integer division by 10 removes the rightmost digit (126 // 10 is 12).

# This function has to be recursive; you may not use loops!

# This function takes in one integer and returns one integer.

# def sumDigits(N):
#     '''
#     N: a non-negative integer
#     '''
#     # Your code here
    
def sumDigits(N):
    '''
    N: a non-negative integer
    '''
    # 等于0的时候输出0
    if N == 0:
        return 0
    else:
        # 否则的话当前最后一个数字加上
        # 少一位的数字的最后一个数字
        return N%10 + sumDigits(N//10)


# Problem 7
# 20.0/20.0 points (graded)
# Write a Python function called satisfiesF that has the specification below. Then make the function call run_satisfiesF(L, satisfiesF). Your code should look like:

# def satisfiesF(L):
#     """
#     Assumes L is a list of strings
#     Assume function f is already defined for you and it maps a string to a Boolean
#     Mutates L such that it contains all of the strings, s, originally in L such
#             that f(s) returns True, and no other elements. Remaining elements in L
#             should be in the same order.
#     Returns the length of L after mutation
#     """
#     # Your function implementation here

# run_satisfiesF(L, satisfiesF)
# For your own testing of satisfiesF, for example, see the following test function f and test code:

# def f(s):
#     return 'a' in s
      
# L = ['a', 'b', 'a']
# print(satisfiesF(L))
# print(L)
# Should print:

# 2
# ['a', 'a']
# Paste your entire function satisfiesF, including the definition, in the box below. After you define your function, make a function call to run_satisfiesF(L, satisfiesF). Do not define f or run_satisfiesF. Do not leave any debugging print statements.

# For this question, you will not be able to see the test cases we run. This problem will test your ability to come up with your own test cases.
def satisfiesF(L):
    """
    Assumes L is a list of strings
    Assume function f is already defined for you and it maps a string to a Boolean
    Mutates L such that it contains all of the strings, s, originally in L such
            that f(s) returns True, and no other elements. Remaining elements in L
            should be in the same order.
    Returns the length of L after mutation
    """
    # Your function implementation here
    targetList = []
    for s in L:
        if f(s):
            targetList.append(s)
    # 切片创建的是新空间，对新空间赋值不影响就空间
    # 所以地址和原来一直
    # L = targetList强夸下，就是引用传递，把targetList的地址给了L
    L[:] = targetList
    return len(targetList)
  
run_satisfiesF(L, satisfiesF) 
