#### Following is the Explanation of the code in this file
1. Import all the required files
```
from urllib.request import urlopen 
This urlopen method is used tto open the url 
```

```
from urllib.request import Request
This request method request the browser for the response
```

```
from bs4 import BeautifulSoup 
This method create help to parse the web page as xml or html
```
```
import re
For some regular expression
```
```
import ssl
For ssl certification
```

2 . Defining a class name web_scraper in that we 
define three function named as 
amazon_page(), wiki_pedia_link_extractors()
and wiki_pedia_headers_extractors()

#### Amazon_page() Function Explanation
```
In this method we first create a variable called
page_request in which we pass two variable 
the url and other the headers for User-Agent request

Secondly create a uclient varaible that has 
a method name urlreq which has two attributes
as page_request and context for ssl verification

Thirdly a soup object in which one is a uclient 
and other is a parser : 'html.parser'
```

#### wiki_pedia_link_extractor Funtion Explanation
```
In this method we first create a variable called
page_request in which we pass two variable 
the url and other the headers for User-Agent request

Secondly create a uclient varaible that has 
a method name urlreq which has two attributes
as page_request and context for ssl verification

Thirdly a soup object in which one is a uclient 
and other is a parser : 'html.parser'

Then we find all the 'a' attributes using findAll method

```

##### wiki_pedia_header_extractor function Explanation
```
In this method we first create a variable called
page_request in which we pass two variable 
the url and other the headers for User-Agent request

Secondly create a uclient varaible that has 
a method name urlreq which has two attributes
as page_request and context for ssl verification

Thirdly a soup object in which one is a uclient 
and other is a parser : 'html.parser'

Then we find all the head tag using find all method


```
