import requests
import urllib
import time
from bs4 import BeautifulSoup

# the url of the webpage that I want to scrape
url = 'http://web.mta.info/developers/turnstile.html'
# connect
response = requests.get(url)

# code to parse the html
soup = BeautifulSoup(response.text,"html.parser")

line_count = 1
# finds all html <a> tags
for tag in soup.findAll('a'):
  if line_count >= 40 and line_count <= 45:
    link = tag['href']

    # downloads link
    download_url = 'http://web.mta.info/developers/'+ link
    urllib.request.urlretrieve(download_url,'./'+link[link.find('/turnstile_')+1:])

    # pauses to prevent spam
    time.sleep(1)
  line_count +=1






