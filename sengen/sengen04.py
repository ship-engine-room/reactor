import random

nouns=["kittie"]
verbs=["meows"]

#takes lists of words (str)
#returns randomly chosen word
def oneOf(wordlist):
    return wordlist[ int( random.random() * len(wordlist) ) ]

#concats noun + verb
def sengen():
    return oneOf(nouns) + " " + oneOf(verbs)

print sengen()
