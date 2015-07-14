#!/usr/bin/python

import reader_v2 as reader
from random import choice
from random import random

KEY_SIZE = 2
FILE = 'sherlock_clean.txt'
NUM_WORDS = 250

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


def add_html( text, book, key_size, num_words ):
    headers = '<DOCTYPE html><html>'
    headers+= '<head><title>Text Generator</title></head><body>'
    footers = '</body></html>'
    
    formatting = '<h1>Markov Chain Based Text Generation</h1>'
    formatting+= '<b>Source text:</b> ' + book + '<br>'
    formatting+= '<b>Words per key:</b> ' + str(key_size) + '<br>'
    formatting+= '<b>Number of words:</b> ' + str(num_words) + '<br>'
    text = headers + formatting + '<p>' + text
    text+= '</p>' + footers
    return text


chains = generate_chains( FILE, KEY_SIZE )
#print chains
text = generate_text( chains, NUM_WORDS, KEY_SIZE )

html = add_html( text, FILE, KEY_SIZE, NUM_WORDS )

if __name__=='__main__':
    print 'Content-type: text/html\n\n'
    print html
