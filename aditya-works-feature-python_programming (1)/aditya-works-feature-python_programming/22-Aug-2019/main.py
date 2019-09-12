from urllib.request import urlopen as urlreq
from urllib.request import Request as req
from bs4 import BeautifulSoup as soup
import re
import ssl
import urllib3

class web_scrapping:
    def amazon_page(self):
        href = []
        title_name = []
        product = {}
        urllib3.disable_warnings()
        my_url = 'https://www.amazon.in/s?k=macbook&ref=nb_sb_noss'
        gcontext = ssl.SSLContext()
        page_request = req(my_url,headers={'User-Agent':'Mozilla/5.0'})
        uclient = urlreq(page_request,context= gcontext).read()
        page_soup = soup(uclient,'html.parser')

        #grab each Link 
        article = page_soup.findAll('div',{'class':'s-include-content-margin'})

        #grab each title
        title = page_soup.findAll('span',{'class':'a-size-medium'})

        for contain in article:
            href.append(contain.a['href'])
        for i in title:
            title_name.append(i)

        #converting it into a dictionary
        for key in title:
            for value in href: 
                product[key] = value
                href.remove(value)
                break
        print("Product with there link : ",product)

    def wiki_pedia_link_extractor(self):
        my_url = 'https://en.wikipedia.org/wiki/Python_(programming_language)'
        gcontext = ssl.SSLContext()

        page_request = req(my_url, headers={'User-Agent':'Mozzila/5.0'})

        uclient = urlreq(page_request,context = gcontext).read()

        page_soup = soup(uclient,'html.parser')

        for link in page_soup.findAll('a',attrs={'href':re.compile("^http://")}):
            print(link['href'])
    def wiki_pedia_header_extractor(self):
        head = []
        my_url = 'https://en.wikipedia.org/wiki/Python_(programming_language)'
        gcontext = ssl.SSLContext()

        page_request = req(my_url,headers={'User-Agent':'Mozilla/5.0'})

        uclient = urlreq(page_request,context= gcontext)

        page_soup = soup(uclient,'html.parser')

        title = page_soup.findAll('title')
        print("The title of the page is : ",title)

        headers = page_soup.findAll(['h1','h2','h3','h4','h4','h6'])
        print(headers)


if __name__ == '__main__':
    

    obj = web_scrapping()
    while True:
        print('1. Amazon-Page-Extractor\n2. WikiPedia-Link-Extractor\n3. WikiPedia-Headers-Extractor')
        choice = input("Enter your choice : ")

        if choice == '1':
                obj.amazon_page()

        elif choice == '2':
                obj.wiki_pedia_link_extractor()

        elif choice == '3':
                obj.wiki_pedia_header_extractor()

        else:
                print('Wrong Choice \n')
                break



    
