#markov chain text generator with two word keys

import fileio_v1 as reader
from random import choice
from random import random

def generate_chains( fname ):
    chains = {}
    text = reader.read_file( fname )
    
    words = text.split()
    i = 0
    while i < len(words) - 2:
        key = words[i] + ' ' + words[i+1]
        value = words[i+2]
        if key in chains:
            chains[ key ].append( value )
        else:
            new_list = []
            new_list.append( value )
            chains[ key ] = new_list
        i+= 1
    #print chains
    return chains


def generate_text( chains, num_words ):
    key = choice( chains.keys() )
    s = key
    i = 0
    while i < num_words:
        word = choice( chains[ key ] )
        s+= ' ' + word
        key = key.split()[-1] + ' ' + word        
        i+= 1
    return s

chains = generate_chains( 'wonderland.txt' )
text = generate_text( chains, 100 )

print chains
print text
