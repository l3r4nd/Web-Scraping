import requests
from bs4 import BeautifulSoup as bs4
import re

def Countries(link):
    '''
    Takes in url as input takes in searches all the Country names
    and removes any special character.
    '''
    r = requests.get(link)
    soup = bs4(r.text, 'html.parser')
    results = soup.find_all('td')
    pat = re.compile('[A-Za-z? ]')
    result = []
    for index in range(0,len(results)-1,3):
        res = results[index].text
        result.append(''.join(re.findall(pat, res)))
    #result.pop(-1)
    return result[:-1]

asia_ = Countries('https://www.whatarethe7continents.com/asia-continent/how-many-countries-in-asia/')
europe_ = Countries('https://www.whatarethe7continents.com/europe/many-countries-europe/')
africa_ = Countries('https://www.whatarethe7continents.com/africa-continent/how-many-countries-in-africa/')
australia_ = Countries('https://www.whatarethe7continents.com/australia/many-countries-australia/')
