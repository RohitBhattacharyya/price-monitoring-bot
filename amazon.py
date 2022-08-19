from bs4 import BeautifulSoup as bs4
import requests


class Amazon:
    def __init__ (self, url, maxPrice: float = False):
        self.url = url
        self.response = requests.get (self.url)
        self.soup = bs4 (self.response.text, 'html.parser')
        self.maxPrice = maxPrice

        self.price = self.getPrice ()
        self.ss = self.find_in_stock ()

    def getPrice (self) -> str:
        ## price_tag = '<span class="a-offscreen">₹824.00</span>'
        price = self.soup.find ('div', {'class': 'a-offscreen'})
        return price.text

    def find_in_stock (self) -> bool or str:
        ## status_tag = '<span class="a-size-medium a-color-success">In stock</span>'
        ## status_tag = '<span class="a-color-price a-text-bold">Currently unavailable</span>'
        status = self.soup.find ('div', {'class': 'a-size-medium a-color-success'})

        if 'sold' in status.text.lower ():
            return False

        if 'in' in status.text.lower () and 'stock' in status.text.lower ():
            return True

    def check_in_range (self) -> bool or str:
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

    def get_info (self) -> dict:
        if self.find_in_stock (): # TRUE
            if self.check_in_range (): # TRUE
                inRange = '\033[92m' + 'In Range' + '\033[0m'

            else: # FALSE
                inRange = 'Out of Range'

            self.info = {'Price' : self.price, 'In Range' : inRange, 'In Stock' : f'\033[92m{"Available"}\033[0m'}

        else: # FALSE
            self.info = {'Price' : self.price, 'In Range' : self.check_in_range (), 'In Stock' : f'\033[91m{"Unavailable"}\033[0m\n'}

        return self.info
