from bs4 import BeautifulSoup as bs4
import requests


class FlipKart:
    def __init__ (self, url: str, maxPrice: float = False):
        self.url = url
        self.response = requests.get (self.url)
        self.soup = bs4 (self.response.text, 'html.parser')
        self.maxPrice = maxPrice

        self.price = self.getPrice ()

    def getPrice (self):
        ## price_tag = '<div class="_30jeq3 _16Jk6d">₹297</div>'
        price = self.soup.find ('div', {'class': '_30jeq3 _16Jk6d'})
        return price.text

    def check_in_range (self):
        price = ''

        for i in range (1, len (self.price)):
            price += self.price [i]

        price = float (price)

        if self.maxPrice:
            if price <= self.maxPrice:
                return True

            else:
                return False

        else:
            return 'Unknown'

    def find_in_stock (self):
        ## status_tag = <div class="_16FRp0">Sold Out</div>
        status = self.soup.find ('div', {'class': '_16FRp0'})

        if 'sold' in status.text.lower ():
            return False

        else:
            return True

    def get_info (self):
        if self.find_in_stock (): # TRUE
            if self.check_in_range (): # TRUE
                inRange = '\033[92m' + 'In Range' + '\033[0m'

            else: # FALSE
                inRange = 'Out of Range'

            self.info = {'Price' : self.price, 'In Range' : inRange, 'In Stock' : f'\033[92m{"Available"}\033[0m'}

        else: # FALSE
            self.info = {'Price' : self.price, 'In Range' : self.check_in_range (), 'In Stock' : f'\033[91m{"Unavailable"}\033[0m\n'}

        return self.info
