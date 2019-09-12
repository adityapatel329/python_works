import requests
url = 'https://readthedocs.org/projects/python-guide/downloads/pdf/latest/'
myfile = requests.get(url, allow_redirects = True)
open('hello.pdf','wb').write(myfile.content)
