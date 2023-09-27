import requests

# URL = "https://api.genderize.io"

name = input('Enter your name: ')
# payload = {'name' : name}

# r = requests.get('https://api.genderize.io/', params=payload)

# print('Guessing your gender based on your name ...')

# gen = r.json()['gender']
# prob = r.json()['probability']
# print('You are a {}'.format(gen))
# print(f'The probability was {prob*100:.0f}%')

def get_age(name):
    URL = "https://api.agify.io/"
    payload = {"name" : name}
    
    r = requests.get(URL, params=payload)
    age = r.json()['age']

    return age

age_value = get_age(name)

print('Guessing your age based on your name ...')
print(f'Your age is {age_value}')

def get_country(name):
    URL = "https://api.nationalize.io"
    payload = {"name" : name}
    
    r = requests.get(URL, params=payload)
    country = r.json()['country'][0]['country_id']

    return country

country_val = get_country(name)

print('Guessing your country based on your name ...')
print(f'Your country is most probably {country_val}')