## Scheduler in Python
* The sched module defines a class which implements a general purpose event
scheduler :
* The scheduler class defines a generic interface to scheduling 
events.
* It needs two functions to actually deal with the "outside world"
-timefunc should be callable without arguments, and return a number
* The delayfunc function should be callable with one argument, compatible 
with the output of timefunc, and should delay that many time units.
* delayfunc will also be called with the argument 0 after each event 
is run to allow other threads an opportunity to run in multi-threaded
applications.

## Scheduler Objects
* scheduler instances have the following methods and attributes:

#### scheduler.enterabs(time,priority,action,arguments=(),kwargs={})
* Schedule a new event. The time argument should be a numeric type
compatible with the return value of the timefunc function passed to the 
constructor.
* Events scheduler for the same time will bee executed in the order of 
their priority.
* A lower number represents a higher priority.
* Executing the event means executing action(*argument, **kwargs).
* Argument is a sequence holding the positional arguments for action.
* kwargs is a dictionary holding the keyword arguments for action.
* Return value is an event which may be used for later cancellation of
the event cancel() ). 
#### scheduler.enter(delay, priority,action,argument=(),kwargs={})
* Schedule an event for delay more time units. Other than the relative time, the other
arguments, the effect and the return value are the same as those 
for enterabs().

#### scheduler.cancel(event)
* Remove the event from the queue. if event is not an event currently in the 
queue, this method will rise a ValueError.

#### scheduler.empty()
* Return true if the event queue is empty 

#### scheduler.run(blocking=True)
* Run all scheduled events. This method will wait(using the delayfunc() function
passed to the constructor ) for the next event, then execute it and so on until there 
are no more scheduled events.
* If blocking is false executes the scheduled events due to expire soonest
and then return the deadline of the next scheduled call in the scheduler.
* Either action or delayfunc can raise an exception. In either case, the scheduler
will maintain a consistent state and propagate the exception. If an exception is raised
by action, the event will not be attempted in future calls to run().

## Web Access Using Python
* urllib is a package that collects several modules for working with URLs:
1. urllib.request for opening and reading URLs
2. urllib.error containing the exceptions raised by urllib.request
3. urllib.parse for parsing URLs
4. urllib.robotparser for parsing robots.txt files

#### 1. urllib.request :
module defines function and classes which help in opening 
URLs(mostly HTTP) in a complex world - basic and digest authentication, redirections,
cookies and more.
* The urllib.request module defines the following functions:
urllib.request.urlopen(url,data=None, [timeout,]*, cafile=None,capath=None, cadefault = False, context = None)
* Open the URL url, which can be either a string or a Request object.
* data must be an object specifying additional data to be sent to the server, or None
 if no such data is needed See Request for details.
* urllib.request module uses HTTP/1.1 and includes Connection:close header in its
HTTP requests.

#### 2. urllib.error
* The urllib.error module defines the exception classes for exceptions raised by 
urllib.request. The base exception class is URLError.
* The following exception are raised by urllib.error as appropriate:
exception urllib.error.URLError
The handler raise this exception when they run into a problem
it is a subclass of OSError.
reason
* The reason for this error. It can be a message string or another exception
instance.
exception urllib.error.HTTPError
* Though being an exception an HTTPError can also function as 
non-exceptional file-like return value. This is useful when handling 
exotic HTTP errors, such as request for authentication.
#### 3. urllib.parse
* This module defines a standard interface to break Uniform Resource Locator
stings up in components to combine the components back into a URL
string, and to convert a "relative URL" to an absolute URL given a "base URL"
## Web Scraping using Python
* Web scraping is a term used to describe the use of a programs
or algorithm to extract and process large amounts of data from web.
* Whether you are a data scientist, engineer, or anybody who analyzes large 
amount of datasets, the ability to scrape data from the web is a useful skill to have.
* Let's say you find data from the web, and there is no direct way tp download it, web scraping
using Python is a skill you can use to extract the data into a useful form that can be imported.
```
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
``` 
* To perform web scraping, you should also import the libraries shown below.
The urllib.request module is used to open URLs.
* The Beautiful Soup package is used to extract data from html files.
* The Beautiful Soup library's name is bs4 which stands for Beautiful Soup,
version 4.
```
from urllib.request import urlopen
from bs4 import BeautifulSoup
```
* After importing necessary modules, you should specify the URL containing 
the dataset and pass it to urlopen() to get rhe html of the page.
```
url = "https://www.datacamp.com/community/tutorials/web-scraping-using-python"
html = urlopen(url)
```
*  Getting the html of the page is just the first step.
* Next step is to create Beautiful Soup object from the html.
* This is done by passing the html to the BeautifulSoup() function.
* The Beautiful Soup package is used to parse the html, that is, take the raw
html text and break it into Python objects.
* The second argument 'lxml' is the html parser whose details you do not need
to worry about at this point.
```
soup = BeautifulSoup(html, 'lxml')
type(soup)

Output:
bs4.BeautifulSoup
```
* The soup object allows you to extract interesting information about 
the website you're scraping such as getting the title of the page as show below:
```
title = soup.title
print(title)
Output:
<title class="next-head">Tutorials - Online Data Analysis &amp; Interpretation | DataCamp</title>
```
* You can also get the text of the web page and quickly 
print it out to check if it is what you except.
```
text = soup.get_text()
```
* You can use the find_all() method of soup to extract useful 
html tags within a web page.
* Examples of useful tags include <a> for hyperlinks,
```
<table> for tables, <tr> for table rows, <th> for table headers,
and <td> for table cells.
```
```
soup.find_all('a')
```
* As you can see from the output above the html tags sometimes
come with attributes such as class src, etc.
* These attributes provide additional information about 
html elements. You can use a for loop and the get("href")
method to extract and print out only hyperlinks.

## Download Activity using Python
#### Using Request 
* You can download file from a URL using the request module.
Consider the code below:
```
import requests

url = 'https://www.python.org/static/img/python-logo@2x.png'
myfile = request.get(url)
open('Download1.png','wb').write(myfile.content)
```
* Simply get the URL using the get method of request module and store 
the request into a variable name "myfile", Then you write the 
contents of the variable into a file.

#### Using wget
* You can also download a file from a URL by using the wget
module of Python.

#### Download File that Redirects
* In this section you will learn to download from a URL, which redirects
to another URL with a .pdf file using requests. The URL reads as follows:
```
https://readthedocs.org/projects/python-guide/downloads/pdf/latest
```
#### To download this pdf file, use the following code:
* In this code the first step we specify is the URL. Then, we use the get
method of the request's module to fetch the URL.
* In this get method, we set the allow_redirects to True, which will allow
redirection in the URL, and the content after redirection will be assigned to the 
variable myfile.

#### Download Multiple Files 
* We will import os and the time modules to check how much time it 
takes to download files. The module ThreadPool lets you run multiple 
threads or process using the pool.
* Let's create a simple function that sends the response to a file in chunks:
#### Download a WebPage Using urllib
* In this section, we will be downloading a webpage using the urllib.
* The urllib library is a standard library of Python, so you do not need
to install it.
```
urllib.request.urlretrieve('url','path')
```
* Specify the URL here that you want to save as and where you want 
to store it :
```
urllib.requests.urlretrieve('https://www.python.org/','c:/users/LikeGeeks/documents/PythonOrganization.html')
```
#### Download via Proxy
* If you need to use a proxy to download your files, you 
can use the ProxyHandler of the urllib module.
```
import urllib.requests
myproxy = urllib.request.ProxyHandler({'http':'127.0.0.2'})
openproxy = urllib.request.build_opener(myproxy)
urllib.requests.urlretrieve('https://www.python.org/')
```

## Search Engine Access Using Python
* Let's say you are working on a project that needs to do web scraping
but you don't know websites on which scraping is to be performed 
beforehand instead you are required to perform google search and then 
proceed according to google search result to few website.
* One way of achieving this is using request and beautiful soup
which has been discussed here in implementing web scraping 
in python with BeautifulSoup
* Instead of putting so much efforts for a trivial task google 
package has been made. its almost a one linear solution to find links of all
the google search result directly.
* Using python package google we can get result of google 
search from python script. We can get link of first n search results.
Required Function and its parameters
```
search(query, tld= 'com',lang='en', num = 10,start=0,stop=None,pause=2.0)
```
* query : query string that we want to search for
* tld : tld stands for top level domain which means we want to search our
result on google.com or google.in or some other domain.
* lang : lang stands for language
* num : Number of results we want
* start : First result to retrieve
* stop : Last result to retrieve Use none to keep searching
forever.
* pause : Lapse to wait between HTTP requests. Lapse too short
may cause Google to block your IP. Keeping significant lapse
will make your program slow but its safe and better option.
* Return : Generator that yields found URLs, if the stop
parameter is None the iterator will loop forever.
## Sending and Receiving email using Python 
* Python comes with built-in smtplib module for sending emails
using simple Mail Transfer Protocol (SMTP). 
* stmplib uses the RFC 821 protocol for SMTP.
* if you decide to use a Gmail account to send your emails, I highly 
recommend setting up a throw away account for the development of your code.
* This is because you''ll have to abjust your Gmail account's security 
settings to allow access from your python code, and because
there's a change you might accidentally expose your login details.
* Also, I found that the inbox of my testing account rapidly filled
up with test emails,which is reason enough to set up a new Gmail account
for development.
#### Sending Fancy Emails
* Python built-in email package allows you to structure
more fancy emails, which can then be transferred with 
smptlib as you have done already.
* Below, you'll learn how use the email package to send
emails with HTML content and attachments.
#### Including HTML content
* If you want to format the text in you email or if you want to
add any images, hyperlinks, or responsive content, then HTML comes in very
handy.
* As not all email clients display HTML content by default, and some people
choose only to receive plain-text emails for security reasons, it is important
to include a plain=text alternative for HTML messages.
* As email client will render the last multipart attachment first, make sure
to add the HTML message after the plain-text version.

