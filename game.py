


class Game:

      """
      The Game object provides the scheme to store the individual game.
      Parameters:
      ----------
      No parameters are passed.
      Attributes:
      ----------
       GameNo(int):The is where we store current game number.
       Word(str):The is where we store current guessing word.
       Status(str):The is where we store Status of the current game.
       BadGuess(int):The is where we store number of bad guess by the user in the curret game.
       MissedLetters(int):The is where we store number of missed guess letters by the usere in  the current game.
       Totalrequestletters(int):The is where we store Total number of the guess letters by the user in  the current game.
       Score(int):The is where we store Score of the user in  the current game.

      """
      GameNo=0
      Word=""
      Status=""
      BadGuess=0
      MissedLetters=0
      Totalrequestletters=0;
      Score=0



      def intialize(self,currGameNo,currWord,currStatus,currBadGuess,currMissedLetters,currTotalrequestletters,currScore):
          """ This function fills the details to used for the reporting.

                                  parameters:
                                  currGameNo(int):The current game number.
                                  currWord(str):The current guessing word.
                                  currStatus(str):The Status of the current game.
                                  currBadGuess(int):The number of bad guess by the user in the curret game.
                                  currMissedLetters(int):The number of missed guess letters by the usere in  the current game.
                                  currTotalrequestletters(int):The Total number of the guess letters by the user in  the current game.
                                  currScore(int):The Score of the user in  the current game.
                                       Nothing.
                                  Returns:
                                       Nothing.
                                  """
          self.GameNo=currGameNo
          self.Word=currWord
          self.Status=currStatus
          self.BadGuess=currBadGuess
          self.MissedLetters=currMissedLetters
          self.Totalrequestletters=currTotalrequestletters
          self.Score=currScore
          return

listofreport=[]
pointsTable=[]


def addGameReport(currGameNo,currWord,currStatus,currBadGuess,currMissedLetters,currTotalrequestletters,currScore):


    """ This function add Single games to the final report collection.

                        parameters:
                        currGameNo(int):The current game number.
                        currWord(str):The current guessing word.
                        currStatus(str):The Status of the current game.
                        currBadGuess(int):The number of bad guess by the user in the curret game.
                        currMissedLetters(int):The number of missed guess letters by the usere in  the current game.
                        currTotalrequestletters(int):The Total number of the guess letters by the user in  the current game.
                        currScore(int):The Score of the user in  the current game.
                             Nothing.
                        Returns:
                             Nothing.
                        """



    Gameobj=Game()
    if(int(currTotalrequestletters)==0):
        currScore=currScore
    else:
        currScore=(currScore)/(currTotalrequestletters)

    if (int(currBadGuess) == 0):
        currScore = currScore
    else:
        currScore = currScore - currScore * (((currBadGuess * 10) / 100))

    Gameobj.intialize(currGameNo,currWord,currStatus,currBadGuess,currMissedLetters,currTotalrequestletters,currScore)
    listofreport.append(Gameobj)


def printer():


   """ This function prints the score report of the user.

                      parameters:
                           Nothing.
                      Returns:
                           Nothing.
                      """


   print("Game    Word      Status   Bad Guesses   Missed Letters   Score")
   print("----    ----      ------   -----------   --------------   -----")
   for Game in listofreport:
        print(str(Game.GameNo)+"       "+str(Game.Word)+"      "+str(Game.Status)+"         "+str(Game.BadGuess)+"           "
            +str(Game.MissedLetters)+"             "+str(int(Game.Score)))


