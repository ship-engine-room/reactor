#markov chain text generator with one word keys

import fileio_v1 as reader
from random import choice
from random import random

def generate_chains( fname ):
    chains = {}
    text = reader.read_file( fname )
    
    words = text.split()
    i = 0
    while i < len(words) - 1:
        if words[i] in chains:
            chains[ words[i] ].append( words[i+1] )
        else:
            new_list = []
            new_list.append( words[i+1] )
            chains[ words[i] ] = new_list
        i+= 1
    return chains


def generate_text( chains, num_words ):
    s = ''
    word = chains.keys()[ int(random() * len(chains.keys())) ]
    i = 0
    while i < num_words:
        s+= word + ' '
        word = choice( chains[ word ] )
        i+= 1
    return s

chains = generate_chains( 'wonderland.txt' )
text = generate_text( chains, 100 )

#print chains
print text
