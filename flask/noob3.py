from flask import Flask

noob3 = Flask( __name__ )

HEADERS = '<DOCTYPE html><html><head><title>%s</title></head><body>'
FOOTERS = '</body></html>'

@noob3.route( '/')
def root():
    html = HEADERS %'main page'
    html+= '<h1>Hola!</h1>'
    html+= FOOTERS
    return html

@noob3.route( '/welcome/' )
@noob3.route( '/welcome/<name>')
def welcome( name = 'Bob' ):
    html = HEADERS %'gnomes'
    html+= '<h2>%s, did you remember your underpants?</h2>' %name
    html+= FOOTERS
    return html

if __name__ == '__main__':
    noob3.debug = True
    noob3.run()
