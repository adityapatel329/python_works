try:
    from googlesearch import search

except ImportError:
    print("No module name 'google' found ")

query = "Aditya"

for j in search(query, tld="co.in",num=10,stop=1,pause=2):
    print(j)
