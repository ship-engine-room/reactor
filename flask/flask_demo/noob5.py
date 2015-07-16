from flask import Flask, render_template
from utils import markov_web_v1 as markov

BOOK_DIR = 'utils/data/'

noob5 = Flask( __name__ )

@noob5.route('/base')
def base():
    return render_template( "base.html", title='base')

@noob5.route( '/')
def root():
    return render_template( 'main.html', title = 'Main Page' )

@noob5.route( '/welcome/' )
@noob5.route( '/welcome/<name>')
def welcome( name = 'Bob' ):
    return render_template( 'welcome.html', person = name, title = 'Gnomes' )


@noob5.route( '/book/' )
@noob5.route( '/book/<source>' )
def book( source = 'war' ):
    text = 'war_of_the_worlds_clean.txt'
    title = 'The War of the Worlds'
    if source == 'sherlock':
        text = 'sherlock_clean.txt'
        title = 'The Adventures of Sherlock Holmes'
    elif source == 'alice':        
        text == 'wonderland_clean.txt'
        title = "Alice's Adventures in Wonderland"

    chains = markov.generate_chains( BOOK_DIR + text, 2 )
    content = markov.generate_text( chains, 200, 2 )
    return render_template( 'markov.html', title='markov', source = title, text = content )

if __name__ == '__main__':
    noob5.debug = True
    noob5.run()
