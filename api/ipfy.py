import requests
import random

class RandomUser():

    def __init__(self):
        self.url = 'https://randomuser.me/api/'

    def get_name_and_gen(self):
        r = requests.get(self.url)
        name = r.json()['results'][0]['name']['first']
        gen = r.json()['results'][0]['gender']

        return name, gen
    

    def assess(self):
        data = RandomUser().get_name_and_gen()
        print(data[0])

        guess_gen = input('Guess the gender of this person (male/female): ')

        if data[1] == guess_gen:
            print(f'You guessed it right! {data[0]} is a {data[1]}')
        else:
            print('Unlucky :(')


# RandomUser().assess()

class IpData():

    def __init__(self):
        self.url = 'https://ipinfo.io/'
        self.url2 = 'https://api.ipify.org/?format=json'

    def get_my_ip(self):
        r = requests.get(self.url2)
        ip = r.json()['ip']

        return ip

    def get_data(self):
        ip = input('Adj meg egy ip címet: ')
        
        if ip == '':
            ip = IpData().get_my_ip()
        
        r = requests.get(self.url+ip+'/geo')
        data = r.json()

        city = data['city']
        country = data['country']

        print(f'Ez az ip cím {city} városban és {country} országban van.')



# IpData().get_data()


class DadJoke():

    def __init__(self):
        self.url = 'https://icanhazdadjoke.com/search'

    def except_joke(self):
        r = requests.get(self.url, headers={'Accept':'application/json'})
        joke = r.json()['results']
        print('There is no joke containing this term but here is a random one:\n')
        return random.choice(joke)['joke']
    
    def get_joke(self):
        phrase = input('Enter a term: ')
        payload = {'term' : phrase}
        
        try:
            r = requests.get(self.url, params=payload, headers={'Accept':'application/json'})
            joke = r.json()['results']
            return random.choice(joke)['joke']
        except:      
            return DadJoke().except_joke()
        
         
print(DadJoke().get_joke())