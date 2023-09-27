import requests
from pprint import pprint

# 1. feladat
URL = 'http://universities.hipolabs.com/search'
A = 'y'

while A == 'y':
    country = input('Enter a country: ')
    name = input('Enter a name: ')
    payload = {'country':country, 'name': name}

    resp = requests.get(URL, params=payload)
    egyetemek = resp.json()

    for i in egyetemek:
        print(i['name'],':', i['web_pages'][0])
    print(resp.url)
    A = input('Akarsz keresni új egyetemet? y/n: ')


# 2. feladat
URL2 = 'https://sulipy.hu/'

r = requests.get(URL2)
print(r.headers['Last-Modified'])




# url = requests.get('https://catfact.ninja/fact')

# fact = url.json()['fact']
# print(fact)

# url = requests.get("https://catfact.ninja/facts")

# facts = url.json()
# pprint(facts)

# for i in facts['data']:
#     print(i['fact'])

# URL = 'http://universities.hipolabs.com/search'

# payload = {'country':'hungary', 'name':'budapest'}

# r = requests.get(URL, params=payload)

# unis = r.json()

# for i in unis:
#     pprint(i)

# print(r.url)


