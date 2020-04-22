# 0x04. AirBnB clone - Web framework

## Resources

* https://jeffknupp.com/blog/2014/03/03/what-is-a-web-framework/
* https://flask.palletsprojects.com/en/1.1.x/quickstart/
* https://flask.palletsprojects.com/en/1.1.x/api/#flask.Flask
* https://jinja.palletsprojects.com/en/2.11.x/templates/
* https://palletsprojects.com/p/flask/

## Tasks

### 0. Hello Flask!
Write a script that starts a Flask web application:

* Your web application must be listening on 0.0.0.0, port 5000
* Routes:
    * /: display “Hello HBNB!”
* You must use the option strict_slashes=False in your route definition

### 1. HBNB
Write a script that starts a Flask web application:

* Your web application must be listening on 0.0.0.0, port 5000
* Routes:
    * /: display “Hello HBNB!”
    * /hbnb: display “HBNB”
* You must use the option strict_slashes=False in your route definition

### 2. C is fun! 
Write a script that starts a Flask web application:

* Your web application must be listening on 0.0.0.0, port 5000
* Routes:
    * /: display “Hello HBNB!”
    * /hbnb: display “HBNB”
    * /c/<text>: display “C ” followed by the value of the text variable (replace underscore _ symbols with a space )
* You must use the option strict_slashes=False in your route definition

### 3. Python is cool! 
Write a script that starts a Flask web application:

* Your web application must be listening on 0.0.0.0, port 5000
* Routes:
    * /: display “Hello HBNB!”
    * /hbnb: display “HBNB”
    * /c/<text>: display “C ”, followed by the value of the text variable (replace underscore _ symbols with a space )
    * /python/(<text>): display “Python ”, followed by the value of the text variable (replace underscore _ symbols with a space )
        * The default value of text is “is cool”
* You must use the option strict_slashes=False in your route definition