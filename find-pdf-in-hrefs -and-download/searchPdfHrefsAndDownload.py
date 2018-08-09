import urllib3
    
from bs4 import BeautifulSoup
from requests import get


#teste comm
_URL="http://galdino.sytes.net:8080/04_Documents/Casa%20do%20Codigo/" 

urls = []
names = []


def main():
    
    http = urllib3.PoolManager()
    html = http.request('GET', _URL)
    soup = BeautifulSoup(html.data)

    for i, link in enumerate(soup.findAll('a')):
        _FULLURL = _URL + link.get('href',None)
        if _FULLURL.endswith('.pdf'):
            urls.append(_FULLURL)
            names.append(soup.select('a')[i].attrs['href'])

    names_urls = zip(names, urls)

    for name, url in names_urls:
        print(url) 
        download(url,name)  

def download(url, file_name):
    # open in binary mode
    with open(file_name, "wb") as file:
        # get request
        response = get(url)
        # write to file
        file.write(response.content)


if __name__ == "__main__":
    main()
