import os

mainDir = os.path.dirname (os.path.abspath (__file__))
pkgs = {'bs4' : 'beautifulsoup4', 'requests' : 'requests', 'csv' : 'python-csv', 'pandas' : 'pandas', 'sqlite3' : 'pysqlite3'}

os.chdir (mainDir)

def main (pkgs = pkgs):
    # check if pkgs a list or dict
    if isinstance (pkgs, list):
        for pkg in pkgs:
            try :
                exec (f"import {pkg}")

            except ModuleNotFoundError:
                os.system ('source bin/activate')
                os.system (f"pip install -r requrements.txt")

    elif isinstance (pkgs, dict):
        for pkg in pkgs:
            try :
                exec (f"import {pkg}")

            except ModuleNotFoundError:
                os.system ('source bin/activate')
                os.system (f"pip install {pkgs [pkg]}")

if __name__ == '__main__':
    main ()

# THE END
