
import random

file=open("four_letters.txt")

values=file.read()

collection=values.split()
limit=len(collection)



def sendGuessWord():
    """ This function returns the randomly selected word from the collection.

                    parameters:
                        Nothing.
                    Returns:
                         collection[random.randrange(limit)](str):randomly selected word.
                    """
    return collection[random.randrange(limit)]
