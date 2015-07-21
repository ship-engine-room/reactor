import urllib2
import bs4 as  bs4hsoup
import json

def get_times():
    u = urllib2.urlopen("http://api.nytimes.com/svc/search/v2/articlesearch.json?q=killer+turtles&api-key=sample-key")
    text = u.read()
    return json.loads(text)

def get_gut():
    u = urllib2.urlopen("http://www.gutenberg.org/ebooks/search/?query=cyrano&go=Go")
    text = u.read()
    return text

def get_weather(city="nyc"):
    url="http://api.openweathermap.org/data/2.5/find?q="+city
    u = urllib2.urlopen(url)
    result = u.read();
    w = json.loads(result)
    return w['list'][0]['main']['temp']

def get_turtles():
    url="https://api.flickr.com/services/rest/?method=flickr.photos.search&api_key=f8744b702f07fa11a59b9fec82ead4b3&tags=turtles&format=json&nojsoncallback=1&api_sig=f9ff829d9ca13267749bf979fef0c620"
    u = urllib2.urlopen(url)
    result = u.read()
    d = json.loads(result)
    return d['photos']['photo']
    
