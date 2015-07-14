from flask import Flask
import markov_web_v2 as markov

noob = Flask(__name__)

@noob.route( '/' )
def root():
    return "<h1>this is the main landing page</h1>"


#to allow variable URL parts, use inside angle brackets in decorator
@noob.route('/markov/<source_text>')
def gen_markov_text(source_text):
    #diagnostic, placeholder output
    header="<html>"
    footer="</html>"
    outStr="<h3>source text user input: " + source_text + "</h3><br>"
    if source_text=="sherlock":
        outStr += "sherlock foo"
    elif source_text=="sawyer":
        outStr += "sawyer foo"
    else:
        outStr += "invalid source text"
    return header + outStr + footer


if __name__ == "__main__":
    noob.debug=True  #enable only during dev phase
    noob.run() 

