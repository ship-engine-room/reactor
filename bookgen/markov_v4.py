#markov chain text generator with variable key length
#default function values and user inputs

import fileio_v1 as reader
from random import choice
from random import random
import sys

KEY_SIZE = 2
NUM_WORDS = 100
FILE = 'sherlock_clean.txt'

def generate_chains( fname=FILE, key_size=KEY_SIZE ):
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


def generate_text( chains, key_size=KEY_SIZE, num_words=NUM_WORDS ):
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

fname = FILE
key_size = KEY_SIZE
words = NUM_WORDS

if len(sys.argv) == 2:
    fname = sys.argv[1]
elif len(sys.argv) == 3:
    fname = sys.argv[1]
    key_size = int(sys.argv[2])
elif len(sys.argv) == 4:
    fname = sys.argv[1]
    key_size = int(sys.argv[2])
    words = int(sys.argv[3])

chains = generate_chains( fname, key_size )
text = generate_text( chains, key_size, words )

#print chains
print text







