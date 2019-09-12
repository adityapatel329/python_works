import requests
url = 'https://www.youtube.com/watch?v=oDkg1zz6xlw'
myfile = requests.get(url)
open('Download1.mp4','wb').write(myfile.content)
