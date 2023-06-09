# Problem 1 - Word Scores
# 10.0/10.0 points (graded)
# The first step is to implement some code that allows us to calculate the score for a single word. The function getWordScore should accept as input a string of lowercase letters (a word) and return the integer score for that word, using the game's scoring rules.

# A Reminder of the Scoring Rules

# Scoring
# The score for the hand is the sum of the scores for each word formed.

# The score for a word is the sum of the points for letters in the word, multiplied by the length of the word, plus 50 points if all n letters are used on the first word created.

# Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is worth 3, D is worth 2, E is worth 1, and so on. We have defined the dictionary SCRABBLE_LETTER_VALUES that maps each lowercase letter to its Scrabble letter value.

# For example, 'weed' would be worth 32 points ((4+1+1+2) for the four letters, then multiply by len('weed') to get (4+1+1+2)*4 = 32). Be sure to check that the hand actually has 1 'w', 2 'e's, and 1 'd' before scoring the word!

# As another example, if n=7 and you make the word 'waybill' on the first try, it would be worth 155 points (the base score for 'waybill' is (4+1+4+3+1+1+1)*7=105, plus an additional 50 point bonus for using all n letters).


# Hints
# You may assume that the input word is always either a string of lowercase letters, or the empty string "".
# You will want to use the SCRABBLE_LETTER_VALUES dictionary defined at the top of ps4a.py. You should not change its value.
# Do not assume that there are always 7 letters in a hand! The parameter n is the number of letters required for a bonus score (the maximum number of letters in the hand). Our goal is to keep the code modular - if you want to try playing your word game with n=10 or n=4, you will be able to do it by simply changing the value of HAND_SIZE!
# Testing: If this function is implemented properly, and you run test_ps4a.py, you should see that the test_getWordScore() tests pass. Also test your implementation of getWordScore, using some reasonable English words.
# Fill in the code for getWordScore in ps4a.py and be sure you've passed the appropriate tests in test_ps4a.py before pasting your function definition here.

def getWordScore(word, n):
    """
    Returns the score for a word. Assumes the word is a valid word.

    The score for a word is the sum of the points for letters in the
    word, multiplied by the length of the word, PLUS 50 points if all n
    letters are used on the first turn.

    Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is
    worth 3, D is worth 2, E is worth 1, and so on (see SCRABBLE_LETTER_VALUES)

    word: string (lowercase letters)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    returns: int >= 0
    """
    score = 0
    answer = 0
    for letter in word:
        score = score + SCRABBLE_LETTER_VALUES[letter]
    if len(word) == n:
        answer = score * len(word) +50
    else:
        answer = score * len(word)
    return answer


# Problem 2 - Dealing with Hands
# 10.0/10.0 points (graded)
# **Please read this problem entirely!!** The majority of this problem consists of learning how to read code, which is an incredibly useful and important skill. At the end, you will implement a short function. Be sure to take your time on this problem - it may seem easy, but reading someone else's code can be challenging and this is an important exercise.


# Representing hands
# A hand is the set of letters held by a player during the game. The player is initially dealt a set of random letters. For example, the player could start out with the following hand: a, q, l, m, u, i, l. In our program, a hand will be represented as a dictionary: the keys are (lowercase) letters and the values are the number of times the particular letter is repeated in that hand. For example, the above hand would be represented as:

# hand = {'a':1, 'q':1, 'l':2, 'm':1, 'u':1, 'i':1}    
# Notice how the repeated letter 'l' is represented. Remember that with a dictionary, the usual way to access a value is hand['a'], where 'a' is the key we want to find. However, this only works if the key is in the dictionary; otherwise, we get a KeyError. To avoid this, we can use the call hand.get('a',0). This is the "safe" way to access a value if we are not sure the key is in the dictionary. d.get(key,default) returns the value for key if key is in the dictionary d, else default. If default is not given, it returns None, so that this method never raises a KeyError. For example:

# >>> hand['e']
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# KeyError: 'e'
# >>> hand.get('e', 0)
# 0
# Converting words into dictionary representation
# One useful function we've defined for you is getFrequencyDict, defined near the top of ps4a.py. When given a string of letters as an input, it returns a dictionary where the keys are letters and the values are the number of times that letter is represented in the input string. For example:

# >>> getFrequencyDict("hello")
# {'h': 1, 'e': 1, 'l': 2, 'o': 1}
# As you can see, this is the same kind of dictionary we use to represent hands.

# Displaying a hand
# Given a hand represented as a dictionary, we want to display it in a user-friendly way. We have provided the implementation for this in the displayHand function. Take a few minutes right now to read through this function carefully and understand what it does and how it works.

# Generating a random hand
# The hand a player is dealt is a set of letters chosen at random. We provide you with the implementation of a function that generates this random hand, dealHand. The function takes as input a positive integer n, and returns a new object, a hand containing n lowercase letters. Again, take a few minutes (right now!) to read through this function carefully and understand what it does and how it works.

# Removing letters from a hand (you implement this)
# The player starts with a hand, a set of letters. As the player spells out words, letters from this set are used up. For example, the player could start out with the following hand: a, q, l, m, u, i, l. The player could choose to spell the word quail . This would leave the following letters in the player's hand: l, m. Your task is to implement the function updateHand, which takes in two inputs - a hand and a word (string). updateHand uses letters from the hand to spell the word, and then returns a copy of the hand, containing only the letters remaining. For example:

# >>> hand = {'a':1, 'q':1, 'l':2, 'm':1, 'u':1, 'i':1}
# >>> displayHand(hand) # Implemented for you
# a q l l m u i
# >>> hand = updateHand(hand, 'quail') # You implement this function!
# >>> hand
# {'a':0, 'q':0, 'l':1, 'm':1, 'u':0, 'i':0}
# >>> displayHand(hand)
# l m  
# Implement the updateHand function. Make sure this function has no side effects: i.e., it must not mutate the hand passed in. Before pasting your function definition here, be sure you've passed the appropriate tests in test_ps4a.py.

# Hints
# Testing

# Testing: Make sure the test_updateHand() tests pass. You will also want to test your implementation of updateHand with some reasonable inputs.

# Copying Dictionaries

# You may wish to review the ".copy" method of Python dictionaries (review this and other Python dictionary methods here).


# Your implementation of updateHand should be short (ours is 4 lines of code). It does not need to call any helper functions.

def updateHand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    # 爆哭，做了一个小时才明白
    # 这里要值拷贝，要不然会同时更新hand的
    answerD = hand.copy()
    # 只能字符串循环
    # 原因：如果是字典循环，做不到重复字符出现的时候value-1
    # 至少我现在做不到
    for letter in word:
        try:
            # 最关键的一步，想了很久
            # 自己减自己，不是用hand的值减1
            # 因为hand的值一直没更新，减一没用的
            answerD[letter] = answerD[letter] - 1
        # 找不到值的时候，会报KeyError
        except KeyError:
            continue

    return answerD


# Problem 3 - Valid Words
# 10.0/10.0 points (graded)
# At this point, we have written code to generate a random hand and display that hand to the user. We can also ask the user for a word (Python's input) and score the word (using your getWordScore). However, at this point we have not written any code to verify that a word given by a player obeys the rules of the game. A valid word is in the word list; and it is composed entirely of letters from the current hand. Implement the isValidWord function.

# Testing: Make sure the test_isValidWord tests pass. In addition, you will want to test your implementation by calling it multiple times on the same hand - what should the correct behavior be? Additionally, the empty string ('') is not a valid word - if you code this function correctly, you shouldn't need an additional check for this condition.

# Fill in the code for isValidWord in ps4a.py and be sure you've passed the appropriate tests in test_ps4a.py before pasting your function definition here.
def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    tempD = hand.copy()
    if len(word) == 0:
        return False
    if word not in wordList:
        return False
    
    for letter in word:
        try:
            if tempD[letter] == 0:
                return False
            tempD[letter] = tempD[letter] - 1
        except KeyError:
            return False
    return True


# Problem 4 - Hand Length
# 10.0/10.0 points (graded)
# We are now ready to begin writing the code that interacts with the player. We'll be implementing the playHand function. This function allows the user to play out a single hand. First, though, you'll need to implement the helper calculateHandlen function, which can be done in under five lines of code.
def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string int)
    returns: integer
    """
    cout = 0
    for value in hand.values():
        if value == 0:
            continue
        else:
            cout = cout + value
    return(cout)


# Problem 5 - Playing a Hand
# 10.0/10.0 points (graded)
# In ps4a.py, note that in the function playHand, there is a bunch of pseudocode. This pseudocode is provided to help guide you in writing your function. Check out the Why Pseudocode? resource to learn more about the What and Why of Pseudocode before you start coding your solution.

# Note: Do not assume that there will always be 7 letters in a hand! The parameter n represents the size of the hand.

# Testing: Before testing your code in the answer box, try out your implementation as if you were playing the game. Here is some example output of playHand:

# Test Cases
# Case #1

# Function Call:

# wordList = loadWords()
# playHand({'h':1, 'i':1, 'c':1, 'z':1, 'm':2, 'a':1}, wordList, 7)
# Output:
#   Current Hand:  a c i h m m z
#   Enter word, or a "." to indicate that you are finished: him
#   "him" earned 24 points. Total: 24 points
 
#   Current Hand:  a c m z
#   Enter word, or a "." to indicate that you are finished: cam
#   "cam" earned 21 points. Total: 45 points
 
#   Current Hand:  z
#   Enter word, or a "." to indicate that you are finished: .
#   Goodbye! Total score: 45 points.    
# Case #2

# Function Call:

# wordList = loadWords()
# playHand({'w':1, 's':1, 't':2, 'a':1, 'o':1, 'f':1}, wordList, 7)
# Output:
#   Current Hand:  a s t t w f o
#   Enter word, or a "." to indicate that you are finished: tow
#   "tow" earned 18 points. Total: 18 points
 
#   Current Hand:  a s t f
#   Enter word, or a "." to indicate that you are finished: tasf
#   Invalid word, please try again.
 
#   Current Hand:  a s t f
#   Enter word, or a "." to indicate that you are finished: fast
#   "fast" earned 28 points. Total: 46 points 
 
#   Run out of letters. Total score: 46 points.    
# Case #3

# Function Call:

# wordList = loadWords()
# playHand({'n':1, 'e':1, 't':1, 'a':1, 'r':1, 'i':2}, wordList, 7)
# Output:
#   Current Hand: a r e t i i n
#   Enter word, or a "." to indicate that you are finished: inertia
#   "inertia" earned 99 points. Total: 99 points

#   Run out of letters. Total score: 99 points.
# Additional Testing

# Be sure that, in addition to the listed tests, you test the same basic test conditions with varying values of n. n will never be smaller than the number of letters in the hand.
def playHand(hand, wordList, n):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    * The user may input a word or a single period (the string ".") 
      to indicate they're done playing
    * Invalid words are rejected, and a message is displayed asking
      the user to choose another word until they enter a valid word or "."
    * When a valid word is entered, it uses up letters from the hand.
    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.
    * The sum of the word scores is displayed when the hand finishes.
    * The hand finishes when there are no more unused letters or the user
      inputs a "."

      hand: dictionary (string -> int)
      wordList: list of lowercase strings
      n: integer (HAND_SIZE; i.e., hand size required for additional points)
      
    """
    score = 0
    totalScore = 0
    bsingle = False
    # As long as there are still letters left in the hand:
    while len(hand) > 0:
    
        # Display the hand
        print('Current Hand:', end="")
        displayHand(hand)

        # Ask user for input
        userInput = input('Enter word, or a "." to indicate that you are finished:')
        
        # If the input is a single period:
        if userInput == '.':
            # End the game (break out of the loop)
            bsingle = True
            
            break
        # Otherwise (the input is not a single period):
        else:
            # If the word is not valid:
            if not isValidWord(userInput, hand, wordList):
                # Reject invalid word (print a message followed by a blank line)
                print('Invalid word, please try again.')
                print()
                continue
            # Otherwise (the word is valid):
            else:
                # Tell the user how many points the word earned, and the updated total score, in one line followed by a blank line
                score = getWordScore(userInput, n)
                totalScore = totalScore + score
                print('"', userInput, '"', 'earned ',score, 'points. Total:', totalScore, 'points')
                print()
                # Update the hand 
                hand = updateHand(hand, userInput)

        # check value in hand
        for k in list(hand.keys()):
            if hand[k] == 0:
                del hand[k]

    # Game is over (user entered a '.' or ran out of letters), so tell user the total score
    if bsingle:
        print('Goodbye! ', end="")
    else:
        print('Run out of letters.', end="")
    print('Total score:', totalScore, 'points')


# Problem 6 - Playing a Game
# 15.0/15.0 points (graded)
# A game consists of playing multiple hands. We need to implement one final function to complete our word-game program. Write the code that implements the playGame function. You should remove the code that is currently uncommented in the playGame body. Read through the specification and make sure you understand what this function accomplishes. For the game, you should use the HAND_SIZE constant to determine the number of cards in a hand.

# Testing: Try out this implementation as if you were playing the game. Try out different values for HAND_SIZE with your program, and be sure that you can play the wordgame with different hand sizes by modifying only the variable HAND_SIZE.

# Sample Output
# Here is how the game output should look...

        
# Loading word list from file...
#    83667 words loaded.
# Enter n to deal a new hand, r to replay the last hand, or e to end game: r
# You have not played a hand yet. Please play a new hand first!

# Enter n to deal a new hand, r to replay the last hand, or e to end game: n
# Current Hand: p z u t t t o
# Enter word, or a "." to indicate that you are finished: tot
# "tot" earned 9 points. Total: 9 points

# Current Hand: p z u t
# Enter word, or a "." to indicate that you are finished: .
# Goodbye! Total score: 9 points.

# Enter n to deal a new hand, r to replay the last hand, or e to end game: r
# Current Hand: p z u t t t o
# Enter word, or a "." to indicate that you are finished: top
# "top" earned 15 points. Total: 15 points

# Current Hand: z u t t
# Enter word, or a "." to indicate that you are finished: tu
# Invalid word, please try again.

# Current Hand: z u t t
# Enter word, or a "." to indicate that you are finished: .
# Goodbye! Total score: 15 points.

# Enter n to deal a new hand, r to replay the last hand, or e to end game: n
# Current Hand: a q w f f i p
# Enter word, or a "." to indicate that you are finished: paw
# "paw" earned 24 points. Total: 24 points

# Current Hand: q f f i
# Enter word, or a "." to indicate that you are finished: qi
# "qi" earned 22 points. Total: 46 points

# Current Hand: f f
# Enter word, or a "." to indicate that you are finished: .
# Goodbye! Total score: 46 points.

# Enter n to deal a new hand, r to replay the last hand, or e to end game: n
# Current Hand: a r e t i i n
# Enter word, or a "." to indicate that you are finished: inertia
# "inertia" earned 99 points. Total: 99 points.

# Run out of letters. Total score: 99 points.

# Enter n to deal a new hand, r to replay the last hand, or e to end game: x
# Invalid command.
# Enter n to deal a new hand, r to replay the last hand, or e to end game: e
    
      
# Hints about the output

# Be sure to inspect the above sample output carefully - very little is actually printed out in this function specifically. Most of the printed output actually comes from the code you wrote in playHand - be sure that your code is modular and uses function calls to the playHand helper function!

# You should also make calls to the dealHand helper function. You shouldn't make calls to any other helper function that we've written so far - in fact, this function can be written in about 15-20 lines of code.

# Here is the above output, with the output from playHand obscured:

        
# Loading word list from file...
#    83667 words loaded.
# Enter n to deal a new hand, r to replay the last hand, or e to end game: r
# You have not played a hand yet. Please play a new hand first!

# Enter n to deal a new hand, r to replay the last hand, or e to end game: n
# <call to playHand> 

# Enter n to deal a new hand, r to replay the last hand, or e to end game: n
# <call to playHand> 

# Enter n to deal a new hand, r to replay the last hand, or e to end game: n
# <call to playHand> 

# Enter n to deal a new hand, r to replay the last hand, or e to end game: x
# Invalid command.
# Enter n to deal a new hand, r to replay the last hand, or e to end game: e

      
# Hopefully this hint makes the problem seem a bit more approachable.

# Entering Your Code

# Be sure to only paste your definition for playGame in the following box. Do not include any other function definitions.

# A Cool Trick about 'print'

# A cool trick about print: you can make two or more print statements print to the same line! Try out the following code. It will separate the first and second line with a space, and the second and third line with a "?" rather than putting each on a new line.

# print('Hello', end = " ")
# print('world', end="?")
# print('!')
def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
      * If the user inputs 'n', let the user play a new (random) hand.
      * If the user inputs 'r', let the user play the last hand again.
      * If the user inputs 'e', exit the game.
      * If the user inputs anything else, tell them their input was invalid.
 
    2) When done playing the hand, repeat from step 1
    """
    
    bFirst = True
    while True:
        userInput = input('Enter n to deal a new hand, r to replay the last hand, or e to end game:')
        if userInput == 'e':
            break
        elif userInput == 'n':
            hand = dealHand(HAND_SIZE)
            playHand(hand, wordList, HAND_SIZE)
            print()
            bFirst = False
        elif userInput == 'r':
            if bFirst:
                print('You have not played a hand yet. Please play a new hand first!')
                print()
            else:
                playHand(hand, wordList, HAND_SIZE)
        else:
            print('Invalid command.')


# Problem 7 - You and your Computer
# 20.0/20.0 points (graded)
# Now that your computer can choose a word, you need to give the computer the option to play. Write the code that re-implements the playGame function. You will modify the function to behave as described below in the function's comments. As before, you should use the HAND_SIZE constant to determine the number of cards in a hand. Be sure to try out different values for HAND_SIZE with your program.

# Sample Output and Hints
# Here is how the game output should look...

# Enter n to deal a new hand, r to replay the last hand, or e to end game: n

# Enter u to have yourself play, c to have the computer play: u

# Current Hand: a s r e t t t
# Enter word, or a "." to indicate that you are finished: tatters
# "tatters" earned 99 points. Total: 99 points

# Run out of letters. Total score: 99 points.

# Enter n to deal a new hand, r to replay the last hand, or e to end game: r

# Enter u to have yourself play, c to have the computer play: c

# Current Hand:  a s r e t t t
# "stretta" earned 99 points. Total: 99 points

# Total score: 99 points.

# Enter n to deal a new hand, r to replay the last hand, or e to end game: x
# Invalid command.

# Enter n to deal a new hand, r to replay the last hand, or e to end game: n

# Enter u to have yourself play, c to have the computer play: me
# Invalid command.

# Enter u to have yourself play, c to have the computer play: you
# Invalid command.

# Enter u to have yourself play, c to have the computer play: c

# Current Hand:  a c e d x l n
# "axled" earned 65 points. Total: 65 points

# Current Hand:  c n
# Total score: 65 points.

# Enter n to deal a new hand, r to replay the last hand, or e to end game: n

# Enter u to have yourself play, c to have the computer play: u

# Current Hand: a p y h h z o
# Enter word, or a "." to indicate that you are finished: zap 
# "zap" earned 42 points. Total: 42 points

# Current Hand: y h h o
# Enter word, or a "." to indicate that you are finished: oy
# "oy" earned 10 points. Total: 52 points

# Current Hand: h h
# Enter word, or a "." to indicate that you are finished: .
# Goodbye! Total score: 52 points.

# Enter n to deal a new hand, r to replay the last hand, or e to end game: r

# Enter u to have yourself play, c to have the computer play: c

# Current Hand:  a p y h h z o
# "hypha" earned 80 points. Total: 80 points

# Current Hand:  z o
# Total score: 80 points.

# Enter n to deal a new hand, r to replay the last hand, or e to end game: e
# Hints about the output

# Be sure to inspect the above sample output carefully - very little is actually printed out in this function specifically. Most of the printed output actually comes from the code you wrote in playHand and compPlayHand - be sure that your code is modular and uses function calls to these helper functions!

# You should also make calls to the dealHand helper function. You shouldn't make calls to any other helper function that we've written so far - in fact, this function can be written in about 15-20 lines of code.

# Here is the above output, with the output from playHand and compPlayHand obscured:

# Enter n to deal a new hand, r to replay the last hand, or e to end game: r
# You have not played a hand yet. Please play a new hand first!
            
# Enter n to deal a new hand, r to replay the last hand, or e to end game: n

# Enter u to have yourself play, c to have the computer play: u

# <call to playHand> 

# Enter n to deal a new hand, r to replay the last hand, or e to end game: r

# Enter u to have yourself play, c to have the computer play: c

# <call to compPlayHand> 

# Enter n to deal a new hand, r to replay the last hand, or e to end game: x
# Invalid command.

# Enter n to deal a new hand, r to replay the last hand, or e to end game: n

# Enter u to have yourself play, c to have the computer play: me
# Invalid command.

# Enter u to have yourself play, c to have the computer play: you
# Invalid command.

# Enter u to have yourself play, c to have the computer play: c

# <call to compPlayHand> 

# Enter n to deal a new hand, r to replay the last hand, or e to end game: n

# Enter u to have yourself play, c to have the computer play: u

# <call to playHand> 

# Enter n to deal a new hand, r to replay the last hand, or e to end game: r

# Enter u to have yourself play, c to have the computer play: c

# <call to compPlayHand> 

# Enter n to deal a new hand, r to replay the last hand, or e to end game: e
# Hopefully this hint makes the problem seem a bit more approachable.

# A Note On Runtime

# You may notice that things run slowly when the computer plays. This is to be expected. If you want (totally optional!), feel free to investigate ways of making the computer's turn go faster - one way is to preprocess the word list into a dictionary (string -> int) so looking up the score of a word becomes much faster in the compChooseWord function.

# Be careful though - you only want to do this preprocessing one time - probably right after we generate the wordList for you (at the bottom of the file). If you choose to do this, you'll have to modify what inputs your functions take (they'll probably take a word dictionary instead of a word list, for example).

# IMPORTANT:Don't worry about this issue when running your code in the checker below! We load a very small sample wordList (much smaller than 83667 words!) to avoid having your code time out. Your code will work even if you don't implement a form of pre-processing as described.

# Entering Your Code

# Be sure to only paste your definition for playGame from ps4b.py in the following box. Do not include any other function definitions.
def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.
          But if no hand was played, output "You have not played a hand yet. 
          Please play a new hand first!"
        
        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the 
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """
    bFirst = True
    while True:
        userInput = input('Enter n to deal a new hand, r to replay the last hand, or e to end game:')
        if userInput == 'e':
            break
        elif userInput == 'n':
            while True:
                nUserInput = input('Enter u to have yourself play, c to have the computer play:')
                
                if nUserInput == 'u':
                    # hand不应该在外面定义的，要不然每一次循环，得到的hand都是一模一样的
                    hand = dealHand(HAND_SIZE)
                    playHand(hand, wordList, HAND_SIZE)
                    print()
                    break
                elif nUserInput == 'c':
                    hand = dealHand(HAND_SIZE)
                    compPlayHand(hand, wordList, HAND_SIZE)
                    print()
                    break 
                else:
                    print('Invalid command.')
                    continue
            # 只有n模式下进来过，就不是第一次
            bFirst = False
        elif userInput == 'r':
            # 想清楚第一次
            # r模式下，不是只玩一次，而是玩最后一次，可以玩很多次的
            # 只是最后一手重复玩
            if bFirst:
                print('You have not played a hand yet. Please play a new hand first!')
                print()
            else:
                while True:
                    nUserInput = input('Enter u to have yourself play, c to have the computer play:')
                    if nUserInput == 'u':
                        # hand不应该在外面定义的，要不然每一次循环，得到的hand都是一模一样的
                        playHand(hand, wordList, HAND_SIZE)
                        print()
                        break
                    elif nUserInput == 'c':
                        compPlayHand(hand, wordList, HAND_SIZE)
                        print()
                        break 
                    else:
                        print('Invalid command.')
                        continue
        else:
            print('Invalid command.')
            continue
