#DEMO Flask app for login apparatus
from flask import Flask, render_template, request

#hardcode user/pass for development
USER="voo"
PASSWORD="doo"

app = Flask(__name__)


def authenticate( name, passwd ):
    return name==USER and passwd==PASSWORD


@app.route( '/' )
def root():
    return render_template( 'index.html' )


@app.route( '/login', methods = ['POST', 'GET'] )
def login_form():
    if request.method == 'GET':
        return render_template( 'index.html' )
    else:
        input = request.form
        u = input['txt_uname']
        p = input['pwd_upass']

        if u=='' or p=='':
            s='Please enter a username and password'
            return render_template( 'index.html', message = s)
        elif authenticate( u, p ):
            s='HuzzaaH! Access granted.'
            return render_template( 'lobby.html', message = s )
        else:
            s='Access denied.'
            return render_template( 'index.html', message = s )


if __name__ == "__main__":
    app.debug=True  #only enable debug mode during dev
    app.run()
    #app.run(host='0.0.0.0') #to listen on all public interfaces
