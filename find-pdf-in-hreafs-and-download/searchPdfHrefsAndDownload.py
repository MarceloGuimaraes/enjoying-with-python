import urllib3
   
from bs4 import BeautifulSoup
from requests import get


#_URL="http://galdino.sytes.net:8080/04_Documents/Casa%20do%20Codigo/" 
_URL="https://ts.accenture.com/sites/Agile101/Agile%20Participant%20Training%20Materials/Forms/AllItems.aspx?RootFolder=%2Fsites%2FAgile101%2FAgile%20Participant%20Training%20Materials%2FAgile%20Delivery%20School%2FDay%201%2FPresentations"

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
    with open(file_name, "wb") as file:
        response = get(url,'utf-8')
        file.write(response.content)


if __name__ == "__main__":
    main()
