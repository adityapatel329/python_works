import os
import requests
from time import time
from multiprocessing.pool import ThreadPool

def url_response(url):

    path, url = url

    r = requests.get(url, stream = True)

    with open(path, 'wb') as f:
        for ch in r:
            f.write(ch)


urls = [("Event1.ws", "https://www.python.org/events/python-events/805/"),
("Event2.ws", "https://www.python.org/events/python-events/801/"),
("Event3.ws", "https://www.python.org/events/python-events/790/"),
("Event4.ws", "https://www.python.org/events/python-events/798/"),
("Event5.ws", "https://www.python.org/events/python-events/807/"),
("Event6.ws", "https://www.python.org/events/python-events/807/"),
("Event7.ws", "https://www.python.org/events/python-events/757/"),
("Event8.ws", "https://www.python.org/events/python-user-group/816/")]

start = time()

for x in urls:
    url_response(x)

print(f"Time to download: {time() - start}")
