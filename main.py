import setup, os
setup.main ()

from flipkart import FlipKart as fk
from amazon import Amazon as az
from dbms_csv import DBMS as dbc
from dbms_sql import DBMS as dbs
from mail import Mailing as mail
from time import sleep


links = open ('links.txt', 'r').readlines ()
#links = dbc (dbPath = os.path.join (setup.mainDir, 'Database'), tableName = 'links.txt').read_data () # 0 = item number, 1 = link, 2 = Escape, 3 = price limit
m = mail ()

gap = 1


def search (link: str, range: float = False):
    if 'tutorial' in link.lower ():
        pass

    if 'flipkart' in link.lower ():
        fk_obj = fk (link, range)
        return fk_obj.get_info ()

    if 'amazon' in link.lower ():
        az_obj = az (link)
        return az_obj.get_info ()


def main ():
    while True:
        try:
            for i in range (0, len (links)):
                link = links [i]
                inf = search (link, 250.0)
                #m.createMsg (inf ['Name'], inf ['Price'], '₹250.0', '0', True)
                sleep (gap)

        except KeyboardInterrupt:
            break


if __name__ == '__main__':
    os.system ('source bin/activate')
    main ()
    os.system ('deactivate')


# THE END
