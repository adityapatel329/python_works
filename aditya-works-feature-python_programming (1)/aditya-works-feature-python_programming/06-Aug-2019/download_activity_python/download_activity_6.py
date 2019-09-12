import urllib.request

myproxy = urllib.request.ProxyHandler({'http':'127.0.0.2'})
openproxy = urllib.request.build_opener(myproxy)
urllib.request.urlretrieve('https://www.python.org/')
