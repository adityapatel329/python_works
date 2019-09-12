from urllib.parse import urlparse
o = urlparse('https://mail.google.com/mail/u/1/?ogbl#inbox')
print(o.scheme)
print(o.port)
#print(o.geturl())
print(o.netloc)
print(o.password)
