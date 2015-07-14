from flask import Flask

noob = Flask( __name__ )

@noob.route( '/')
def root():
    return '<h1>Hola!</h1>'

@noob.route( '/welcome' )
def welcome():
    return 'underpants'


if __name__ == '__main__':

    noob.debug = True
    noob.run()
