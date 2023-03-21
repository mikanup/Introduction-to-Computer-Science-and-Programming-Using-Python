# Problem 1 - Is the Word Guessed
# Please read the Hangman Introduction before starting this problem. We'll start by writing 3 simple functions that will help us easily code the Hangman problem. First, implement the function isWordGuessed that takes in two parameters - a string, secretWord, and a list of letters, lettersGuessed. This function returns a boolean - True if secretWord has been guessed (ie, all the letters of secretWord are in lettersGuessed) and False otherwise.

# Example Usage:

# >>> secretWord = 'apple' 
# >>> lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
# >>> print(isWordGuessed(secretWord, lettersGuessed))
# False
# For this function, you may assume that all the letters in secretWord and lettersGuessed are lowercase.

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    for i in secretWord:
      if not i in lettersGuessed:
        return False
    return True


# Problem 2 - Getting the User's Guess
# Next, implement the function getGuessedWord that takes in two parameters - a string, secretWord, and a list of letters, lettersGuessed. This function returns a string that is comprised of letters and underscores, based on what letters in lettersGuessed are in secretWord. This shouldn't be too different from isWordGuessed!

# Example Usage:

# >>> secretWord = 'apple' 
# >>> lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
# >>> print(getGuessedWord(secretWord, lettersGuessed))
# '_ pp_ e'
# When inserting underscores into your string, it's a good idea to add at least a space after each one, so it's clear to the user how many unguessed letters are left in the string (compare the readability of ____ with _ _ _ _ ). This is called usability - it's very important, when programming, to consider the usability of your program. If users find your program difficult to understand or operate, they won't use it!

# For this problem, you are free to use spacing in any way you wish - our grader will only check that the letters and underscores are in the proper order; it will not look at spacing. We do encourage you to think about usability when designing.

# For this function, you may assume that all the letters in secretWord and lettersGuessed are lowercase.

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    targetStr = ''
    blank = '_ '
    for i in secretWord:
      if i in lettersGuessed:
        targetStr = targetStr + i
      else:
        targetStr = targetStr + blank
    return targetStr


# Problem 3 - Printing Out all Available Letters
# Next, implement the function getAvailableLetters that takes in one parameter - a list of letters, lettersGuessed. This function returns a string that is comprised of lowercase English letters - all lowercase English letters that are not in lettersGuessed.

# Example Usage:

# >>> lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
# >>> print(getAvailableLetters(lettersGuessed))
# abcdfghjlmnoqtuvwxyz
# Note that this function should return the letters in alphabetical order, as in the example above.

# For this function, you may assume that all the letters in lettersGuessed are lowercase.

# Hint: You might consider using string.ascii_lowercase, which is a string comprised of all lowercase letters:

# >>> import string
# >>> print(string.ascii_lowercase)
# abcdefghijklmnopqrstuvwxyz

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    allLowerLetter = string.ascii_lowercase
    notGuessStr = ''
    for i in allLowerLetter:
      if i not in lettersGuessed:
        notGuessStr = notGuessStr + i
    return notGuessStr


# Problem 4 - The Game
# Now you will implement the function hangman, which takes one parameter - the secretWord the user is to guess. This starts up an interactive game of Hangman between the user and the computer. Be sure you take advantage of the three helper functions, isWordGuessed, getGuessedWord, and getAvailableLetters, that you've defined in the previous part.

# Hints:
# You should start by noticing where we're using the provided functions (at the top of ps3_hangman.py) to load the words and pick a random one. Note that the functions loadWords and chooseWord should only be used on your local machine, not in the tutor. When you enter in your solution in the tutor, you only need to give your hangman function.

# Consider using lower() to convert user input to lower case. For example:

# guess = 'A'
# guessInLowerCase = guess.lower()
# Consider writing additional helper functions if you need them!

# There are four important pieces of information you may wish to store:

# secretWord: The word to guess.
# lettersGuessed: The letters that have been guessed so far.
# mistakesMade: The number of incorrect guesses made so far.
# availableLetters: The letters that may still be guessed. Every time a player guesses a letter, the guessed letter must be removed from availableLetters (and if they guess a letter that is not in availableLetters, you should print a message telling them they've already guessed that - so try again!).

# Note that if you choose to use the helper functions isWordGuessed, getGuessedWord, or getAvailableLetters, you do not need to paste your definitions in the box. We have supplied our implementations of these functions for your use in this part of the problem. If you use additional helper functions, you will need to paste those definitions here.

# Your function should include calls to input to get the user's guess.

# Why does my Output Have None at Various Places?

# None is a keyword and it comes from the fact that you are printing the result of a function that does not return anything. For example:

#     def foo(x):
#         print(x)
              
# If you just call the function with foo(3), you will see output:
#     3   #-- because the function printed the variable
            
# However, if you do print(foo(3)), you will see output:
#     3     #-- because the function printed the variable
#     None  #-- because you printed the function (and hence the return)
              
# All functions return something. If a function you write does not return anything (and just prints something to the console), then the default action in Python is to return None

def printLenOfSecretWord(secretWord):
  print("I am thinking of a word that is ", len(secretWord), "letters long.")
  print('-----------')

def isNotWordGuessed(secretWord, lettersGuessed):  
    for i in secretWord:
      if i in lettersGuessed:
        return False
    return True

def printLenOfSecretWord(secretWord):
  print("I am thinking of a word that is ", len(secretWord), "letters long.")
  print('-----------')

def isNotWordGuessed(secretWord, lettersGuessed):  
    for i in secretWord:
      if i in lettersGuessed:
        return False
    return True

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    # wordlist = loadWords()
    # secretWord = chooseWord(wordlist)
    print('Welcome to the game Hangman!')

    # get the length of secretWord
    printLenOfSecretWord(secretWord)
    # init letters of guessed
    lettersGuessed = []
    # user's input
    lGuessed = ''
    # boolean of guessed
    bGuessed = False
    # 回数の初期化
    i = 1
    # 合計の回数
    guessNum = 8
    
    # forループよりwhileのほうがいい
    # 理由：下記の場合、ループ回数に計算されてない
    # 1.Guessed numberはあっている
    # 2.Guessed numberはすでにGuessed
    while i <= guessNum:
      # 残った回数の印刷
      print('You have',guessNum - i + 1,'guesses left.')
      # Guessしてないletterの印刷
      print('Available Letters:',getAvailableLetters(lettersGuessed))
      # ユーザのインプットを取得
      lGuessed = input('Please guess a letter: ')
      # Guessedの内容を出力（Guessed内容存在しない場合、length of secretWordの「_」を出力）
      getGuessedW = getGuessedWord(secretWord, lettersGuessed)

      # インプットしたletterはリストに存在する場合
      if lGuessed in lettersGuessed:
        # すでにGuessedなので、提示メッセージを出力
        print("Oops! You've already guessed that letter:",getGuessedW)
        print('-----------')
        # すでにGuessedなので、回数に計算されない
        # 一番下の「i = i + 1」を実行しない
        continue
      else:
        # そうではない場合、Guessedリストに追加
        lettersGuessed.append(lGuessed)
      
      # Guessedの内容を出力（Guessed内容存在しない場合、length of secretWordの「_」を出力）
      # lettersGuessedは更新したので、再取得必要
      getGuessedW = getGuessedWord(secretWord, lettersGuessed)
      
      # Guessしたリストの判断
      # 判断内容：リストとsecretWordは合っているかどうか（全般）
      if isWordGuessed(secretWord, lettersGuessed):
        print('Good guess:',getGuessedW)
        print('-----------')
        print('Congratulations, you won!')
        # ぴったりする場合、ループ終了
        bGuessed = True
        break
      else:
        # Guess内容はsecretWordに存在しない場合
        if isNotWordGuessed(secretWord, lettersGuessed):
          print('Oops! That letter is not in my word:',getGuessedW)
        else:
          print('Good guess:',getGuessedW)
          # Guess内容は合っている場合、回数に計算されない
          i = i - 1
        print('-----------')
      
      # ループごとに回数の追加
      i = i + 1

    # ループの外に、Guessの判定
    # Falseの場合、Guessしてないメッセージの出力
    if not bGuessed:
      print('Sorry, you ran out of guesses. The word was else. ')