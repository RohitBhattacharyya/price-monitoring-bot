import os
from setup import mainDir, pkgs, gitLink


def rm_dependencies (pkgs: dict = pkgs):
    for pkg in pkgs.keys ():
        try:
            exec (f'import {pkg}')
            os.system (f'pip uninstall {pkg}')

        except ImportError:
            continue


def kill ():
    print ('Removing dependencies.')
    rm_dependencies ()
    print ('Dependencies removed.')

    os.system (f"sudo rm -r '{mainDir}'")
    print ('Bye for now. If you feel like re installing this program, you can install it from the bellow given link.')
    print (f'Link: {gitLink}')

    exit ()


if __name__ == '__main__':
    kill ()


# THE END
