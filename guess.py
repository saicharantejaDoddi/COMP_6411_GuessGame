import sys
import game
import stringDataBase

# Score Managing logic  Start

listofreport={"a":8.17,"b":1.49,"c":2.78,"d":4.25,"e":12.70,"f":2.23,"g":2.02,"h":6.09,"i":6.97,"j":0.15,"k":0.77,"l":4.03,"m":2.41,"n":6.75,"o":7.51,"p":1.93,"q":0.10,"r":5.99,"s":6.33,"t":9.06,"u":2.76,"v":0.98,"w":2.36,"x":0.15,"y":1.97,"z":0.07}


def wordToScore(findscoreWord):

    """ Returns The Summation of the frequency value of the word.

    parameters:

     findscoreWord(str):The word for which you need the Summation.

    Returns:
        score(float):The Summation Value of the word.
    """

    global listofreport
    score=float(0)
    for singlechar in findscoreWord:
        score=score+float(str(listofreport[singlechar]))
    return score

def charScore(findscorechar):

    """ Returns The Value of the sent Dictionary key.

        parameters:

         findscorechar(str):The Key for which we need to know the value.

        Returns:
            score(float):The Value of the Key.
        """

    global listofreport
    score=float(0)
    score=float(str(listofreport[findscorechar]))
    return score
# Score Managing logic  end

# Global variables start

# Report Globals
playedGames=1
currGameNo = 1
currWord = ""
currStatus = ""
currBadGuess = 0
currMissedLetters = 0
currTotalrequestletters=0
currScore = 0
# End
GameWords = ["ROSE", "ROOM", "RANA", "ROME", "ROMO"]
GameNow = 0;

GuessWord = stringDataBase.sendGuessWord()
currScore=int(wordToScore(GuessWord))
# print(GuessWord)
Header = """ ** The great guessing game **
\nCurrent Guess:"""
currentGuessHead="\nCurrent Guess:  "
incorrectOption="\nPlease select the correct option\n"
Word = "----"
Options = """
 \ng = guess, t = tell me,l for a letter, and q to quit """
WrongMissedLetter = """
@@@
@@@ You missed the letter
@@@
"""
WrongWord = """
@@@
@@@ Your Guess Word is Wrong
@@@
\n"""
LFullForm = "Enter a letter:"
WFullForm = "Enter the Word:"
LettersFound = 0
FoundWord = """
@@@
@@@You Found the Word 
@@@"""
global counter
counter = 0
DecisionStatus = 0
WordChances = 0


# Global Variables End

# Global Functions Start




def resettheGameGaveup():

    """ This function reset the game when the user gave up.

            parameters:
                 nothing.
            Returns:
                 nothing.
            """

    global GuessWord
    print("\nYou Gave up on this word :" + GuessWord+"\n")
    global currGameNo
    global currStatus
    global currBadGuess
    global currMissedLetters
    global currTotalrequestletters
    global currScore
    global currWord
    game.addGameReport(currGameNo, GuessWord, currStatus, currBadGuess, currMissedLetters,currTotalrequestletters, currScore)
    global playedGames
    playedGames=playedGames+1
    # Report Reset
    currGameNo = currGameNo + 1
    currWord = ""
    currStatus = ""
    currBadGuess = 0
    currMissedLetters = 0
    currTotalrequestletters=0
    currScore = 0
    # End Report
    # Reset the Game Variables Start
    global counter
    counter = 0
    global Word
    Word = "----"
    global LettersFound
    LettersFound = 0
    global GameNow
    GameNow = GameNow + 1;
    # END
    # Reset the Wording
    GuessWord = stringDataBase.sendGuessWord()
    currScore = int(wordToScore(GuessWord))
    #Remove start
    print(GuessWord)
    #Remove end
    print(Header + Word + Options)
    # End  Reset

    return


def resettheGame():

    """ This function reset the game when the user is done with the previous game.

               parameters:
                    nothing.
               Returns:
                    nothing.
               """

    global GuessWord
    print("\nYou finally guessed correct Word :"+GuessWord+"\n"+FoundWord)
    global currGameNo
    global currStatus
    global currBadGuess
    global currMissedLetters
    global currTotalrequestletters
    global currScore
    global currWord

    game.addGameReport(currGameNo, GuessWord, currStatus, currBadGuess, currMissedLetters,currTotalrequestletters, currScore)
    global playedGames
    playedGames = playedGames + 1
    # Report Reset
    currGameNo = currGameNo + 1
    currWord = ""
    currStatus = ""
    currBadGuess = 0
    currMissedLetters = 0
    currTotalrequestletters=0
    currScore = 0

    # End Report
    # Reset the Game Variables Start
    global counter
    counter = 0
    global Word
    Word = "----"
    global LettersFound
    LettersFound = 0
    global GameNow
    GameNow = GameNow + 1;
    # END
    # Reset the Wording
    GuessWord = stringDataBase.sendGuessWord()
    currScore=int(wordToScore(GuessWord))
    print(GuessWord)
    print(Header + Word + Options)
    # End  Reset

    return


def PrintingtheReport():

    """ This function prints the report of the user Score.

                  parameters:
                       nothing.
                  Returns:
                       nothing.
                  """
    game.printer()
    return


def modifiedWord(foundchar, currentWord, GuessWord):

    """ This function prints the report of the user Score.

                  parameters:
                       foundchar(char):This is character correctly guessed by the user.
                       currentWord(str):This is the word which is have masked letters.
                       GuessWord(str):This is word which is to be guessed by the user.
                  Returns:
                       currentWord(str):This is the word which unmasked by the new guessed letter.
                  """

    i = 0
    while i < 4:
        if (GuessWord[i] == foundchar):
            currentWord = currentWord[0:i] + GuessWord[i] + currentWord[i + 1:4]
            i = i + 1
        else:
            i = i + 1
    return currentWord


def guessedWord(currentWord, GuessWord):


    """ This function returns 0 or 1 based on the match of the word guessed and actual word.

                  parameters:
                       currentWord(str):The word which is guessed by the user.
                       GuessWord(str):TThe word which has to be guessed by the user.
                  Returns:
                       desc(int):Returns 1 if the word is gussed correctly.if not 0.
                  """

    desc = 1
    i = 0
    if(len(currentWord)!=4):
       desc=0
       return desc
    else:
        while i < 4:
            if (GuessWord[i] == currentWord[i]):
                desc = 1
                i = i + 1
            else:
                desc = 0
                return desc
    return desc


# Gloable Functions End


# Execution Started
# Remove this end
# print("STARTED")
print(GuessWord)
# print("STARTED")
# Remove this end
print(Header + Word + Options)

while DecisionStatus == 0:

    if playedGames==101:

        print("\nYour reached your maximum guess Games.")
        DecisionStatus=1
        continue
    userInput = input()[0]
    if userInput == "l":
        currTotalrequestletters = currTotalrequestletters + 1
        counter = 0
        print(LFullForm)
        userguessLetter = input()[0]

        for i in Word:
            if i==userguessLetter:
               print("\nYou already guessed it\n"+ Options)
               LettersFound=LettersFound-1
               continue

        for i in GuessWord:
            if i == userguessLetter:
                currScore=currScore-charScore(i)
                counter = counter + 1
                LettersFound = LettersFound + 1
                Word = modifiedWord(userguessLetter, Word, GuessWord)
            else:
                counter = counter
        if (LettersFound == 4):
            # Reset the Game
            currStatus = "Success"
            resettheGame()
            continue
        else:
            print("You Found " + str(counter) + " letter")
        if counter >= 1:
            print(currentGuessHead+Word + Options)
        else:
            currMissedLetters = currMissedLetters + 1

            print(WrongMissedLetter + Options)
    elif userInput == "g":
        print(WFullForm)
        gsWord = input()
        if (guessedWord(gsWord,GuessWord) == 1):
            # Reset the Game
            currStatus = "Success"
            resettheGame()
            continue
        else:
            currBadGuess = currBadGuess + 1;
            print(WrongWord + Options)

    elif userInput == "q":
        PrintingtheReport()
        DecisionStatus = 1
    elif userInput == "t":
        # Reset the Game
        currStatus = "Gave Up"
        currScore=-currScore
        resettheGameGaveup()
        continue
    else:
         print(incorrectOption+Options)
        # DecisionStatus = 1


