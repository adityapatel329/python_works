import requests
import bs4 as bs
import urllib.request
import os


url = str(input('URL: '))
mypath = 'C:\\Users\\Public\\Downloads\\aditya-works\\19-Aug-2019\\imagescrapper\\images'


try:
        
           
        raw = requests.get(url,verify=True).text
        soup = bs.BeautifulSoup(raw,'html.parser')
        

        imgs = soup.find_all('img')

        links = []

        for i in imgs:
                link = i.get('src')
                if 'https://' not in link:
                        link = url + link
                links.append(link)

        print("Images detected:",str(len(links)))

        print(links)
        for i in range(len(links)):
                filename = 'im_{}.png'.format(i)
                fullfilename = os.path.join(mypath,filename)
                urllib.request.urlretrieve(links[i],fullfilename)
                print('Done ! ')

except Exception as e:
        print("Your Error : ",e)
