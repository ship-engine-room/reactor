from flask import Flask

noob2 = Flask( __name__ )

@noob2.route( '/')
def root():
    html = '<h1>Hola!</h1>'    
    return html

@noob2.route( '/welcome/' )
@noob2.route( '/welcome/<name>' )
def welcome(name = 'Bob'):
    clothing = 'socks'
    #html = '<h2>' + name + ', did you remember your underpants?</h2>'
    html = '<h2>%s, did you remember your %s?</h2>' %(name, clothing)
    return html

@noob2.route( '/foo' )
def foo():
    return 'FOOOOOOOOOOO!'

if __name__ == '__main__':
    noob2.debug = True
    noob2.run( host = '0.0.0.0', port = 12345)
