#!/usr/bin/env python3

## Sending stuff via http

# Documentation on the response object
#https://requests.readthedocs.io/en/master/api/#requests.Response


import requests
response = requests.get('https://www.google.com')

# Show the 1st 300 chars of the response
print(response.text[:300])

# Show the 1st 100 chars of the 'raw' response
response = requests.get('https://www.google.com', stream=True)
print(response.raw.read()[:100])

# What's all that? 
# The response was compressed with gzip, so it had to be decompressed before we could even read the text of the HTML. One more thing that the Requests library handled for us!

# The requests.Response object also contains the exact request that was created for us. 
# We can check out the headers stored in our object to see that the Requests module told the web server that it was okay to compress the content:
print("Request headers  - 'Accept-Encoding' is : " + response.request.headers['Accept-Encoding'])

# And then the server told us that the content had actually been compressed.
print("Response headers - 'Content-Encoding' is : " + response.headers['Content-Encoding'])

######################
#

# how do we know if a request we made got a successful response
print('response.ok:' + str(response.ok))

# To write maintainable, stable code, you’ll always want to check your responses to make sure they succeeded before trying to process them further. For example, you could do something like this:
#url='https://www.google.com_thisdoesnotexist'
url='https://www.google.com'
#response = requests.get(url)
#if not response.ok:
#    raise Exception("GET failed with status code {}".format(response.status_code))



# But you don't really need to do that. 
# Requests has us covered here, too! We can use the Response.raise_for_status() method, which will raise an HTTPError exception only if the response wasn’t successful.
# See https://requests.readthedocs.io/en/master/api/#requests.Response.raise_for_status

#url='https://www.google.com_thisdoesnotexist'
url='https://www.google.com'
response = requests.get(url)
response.raise_for_status()

print('response.status_code:' + str(response.status_code))


#######################
#HTTP GET and POST Methods

#HTTP supports several HTTP methods, like GET, POST, PUT, and DELETE. We're going to spend time on the two most common HTTP requests: GET and POST.
#The HTTP GET method, of course, retrieves or gets the resource specified in the URL. By sending a GET request to the web server, you’re asking forthe server to GET the resource for you. When you’re browsing the web, most of what you’re doing is using your web browser to issue a whole bunch of GET requests for the text, images, videos, and so forth that your browser will display to you.

#A GET request can have parameters. Have you ever seen a URL that looked like this?
#https://example.com/path/to/api/cat_pictures?search=grey+kitten&max_results=15
# an example that actually works is
# https://www.bing.com/search?q=cat
#The question mark separates the URL resource from the resource's parameters. 
# These parameters are one or more key-value pairs, formatted as a query string. 
# In the example above, the search parameter is set to "grey+kitten", and the max_results parameter is set to 15.

#But you don't have to write your own code to create an URL like that one. 
# With requests.get(), you can provide a dictionary of parameters, and the Requests module will construct the correct URL for you!

#############################
## USING  GET ############
#############################
url='https://www.bing.com/search'
p = {"q": "cat"}
response = requests.get(url, params=p)
print(response.request.url)

# Shows the query on the url itself
#https://www.bing.com/search?q=cat


#You might notice that using parameters in Requests is yet another form of data serialization. Query strings are handy when we want to send small bits of information, but as our data becomes more complex, it can get hard to represent it using query strings. 
#An alternative in that case is using the HTTP POST method. This method sends, or posts, data to a web service. Whenever you fill a web form and press a button to submit, you're using the POST method to send that data back to the web server. This method tends to be used when there's a bunch of data to transmit.

#In our scripts, a POST request looks very similar to a GET request. Instead of setting the params attribute, which gets turned into a query string and appended to the URL, we use the data attribute, which contains the data that will be sent as part of the POST request.

#############################
## USING  POST    ############
#############################
## Not really a working example, but you get the idea.
url='https://www.bing.com/search'
p = {"description": "white kitten",
      "name": "Snowball",
      "age_months": 6}
response = requests.post(url, data=p)

#Let's check out the generated URL for this request:
print(response.request.url)


#See how much simpler the URL is on this POST now? Where did all of the parameters go? They’re part of the body of the HTTP message. We can see them by checking out the body attribute.
print(response.request.body)

#>>> response.request.body
#'description=white+kitten&name=Snowball&age_months=6'

#Ah, ha! There they are!

#So, if we need to send and receive data from a web service, we can turn our data into dictionaries and then pass that as the data attribute of a POST request.

#Today, it's super common to send and receive data specifically in JSON format, so the Requests module can do the conversion directly for us, using the json parameter.


#>>> response = requests.post("https://example.com/path/to/api", json=p)
#>>> response.request.url
#'https://example.com/path/to/api'
#>>> response.request.body
#b'{"description": "white kitten", "name": "Snowball", "age_months": 6}' 

# Further information
# https://requests.readthedocs.io/en/master/user/quickstart/

#########
#What is Django?
#The lab project at the end of this module will feature a very simple web application created using Django. Django is a full-stack web framework written in Python. For this project, you'll only need to interact with it through HTTP requests, but it's still a good idea to understand what it is, and when it would be a good tool for you to use.

# full-stack web framework handles a bunch of different components that are typical when creating a web application. It contains libraries that help you handle each of the pieces: writing your application's code, storing and retrieving data, receiving web requests, and responding to them. If you need to build an application that has a web frontend, using a web framework like Django can save you a lot of time and effort, because a lot of challenges are already solved for you.

#Web frameworks are commonly split into three basic components: (1) the application code, where you'll add all of your application's logic; (2) the data storage, where you'll configure what data you want to store and how you're storing it; and (3) the web server, where you'll state which pages are served by which logic.

#Splitting your code like that helps you write more modular code, promotes code reuse, and allows for flexibility when viewing and accessing data. For example, you could have a simple web page where users of the system can access the information already stored in it, and a separate programmatic interface that can be used by other scripts or applications to transmit data to the system.

#When you’re writing a web application, there's a ton of little decisions to make. Relying on a framework like Django is similar to using external libraries for your code. There are a lot of features, which you can use very easily, instead of writing everything from scratch and re-making all of the same mistakes that we all make when writing a web application for the first time.

#Django has a ton of useful components for building websites. In the lab project, Django will be used for serving the company website, including customer reviews. It does this by taking the request for a URL and parsing it using the urlresolver module. This is a core module in Django that interprets URL requests and matches them against a list of defined patterns. If a URL matches a pattern, the request is passed to the associated function, called a view. This allows you to serve different pages depending on what URL is being requested. You can even build complex logic into the function handling the request to make more dynamic, interactive, and exciting pages.

#Django can also handle reading and writing data from a database, letting you store and retrieve data used by your application. In the lab, the database holds the customer reviews for the company. When a user loads the website, the logic will ask the database for all available customer reviews. These are retrieved and formatted into a web page, which is served as a response to the URL request. Django makes it easy to interact with data stored in a database by using an object-relational mapper, or ORM. This tool provides an easy mapping between data models defined as Python classes and an underlying database that stores the data in question.

#On top of this, the Django application running in the lab includes an endpoint that can be used to add new customer reviews to the database. This endpoint is configured to receive data in JSON format, sent through an HTTP POST request. The data transmitted will then be stored in the database and added to the list of all reviews. The framework even generates an interactive web form, that lets us directly interact with the endpoint using our browser, which can be really handy for testing and debugging.

#Django is one of many popular web frameworks. Alternative Python-based web frameworks similar to Django include Flask, Bottle, CherryPy, and CubicWeb. There are a host of other frameworks written in other languages too, not just Python.


