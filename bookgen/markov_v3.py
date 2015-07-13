#markov chain text generator with variable key length

import fileio_v1 as reader
from random import choice
from random import random

KEY_SIZE = 2
FILE = 'sherlock_clean.txt'

def generate_chains( fname, key_size ):
    chains = {}
    text = reader.read_file( fname )
    
    words = text.split()
    i = 0
    while i < len(words) - key_size:
        key = ' '.join( words[i : i+key_size] ) 
        value = words[i + key_size]
        if key in chains:
            chains[ key ].append( value )
        else:
            new_list = []
            new_list.append( value )
            chains[ key ] = new_list
        i+= 1
    return chains


def generate_text( chains, num_words, key_size ):
    key = choice( chains.keys() )
    s = key
    i = 0
    while i < num_words:
        word = choice( chains[ key ] )
        s+= ' ' + word
        key = ' '.join(key.split()[1 : key_size + 1])
        if key_size > 1:
            key+= ' '        
        key+= word
        i+= 1
    return s



chains = generate_chains( FILE, KEY_SIZE )
#print chains

text = generate_text( chains, 100, KEY_SIZE )

print text
