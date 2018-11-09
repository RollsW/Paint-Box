import requests
from bs4 import BeautifulSoup as bs
import time

def scrape(iop):
    n = 0
    results = []
    output = []
    while n < 5:
        time.sleep(5) #let's be polite
        n = n+1
        print(f"page {n}")
        r = requests.get(iop+f"twitter/page:{n}")
        results.append(r.text)

    for r in results:
        soup = bs(r,'lxml') #import data
        x = soup.select(".handle") #select only <div id=handle> tags
        x = [i.string for i in x] #remove tags
        output = output+x

    output = list(set(output)) #deduplicate
    return(output)


if __name__ == "__main__":
    info="https://color.adobe.com/explore/?filter=most-popular&time=week"
    r = requests.get(info)

    
    soup = bs(r.text,'lxml')
    x = soup.select(".collection-assets-item") #select only <div id=handle> tags
    print(x)
##    names= []
##    cols = []
##    for i in x:
##        y = soup.select(".content")
##    