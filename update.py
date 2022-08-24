import os
from setup import gitLink


def update ():
    cmd = f'git clone {gitLink}'
    os.system (cmd)


if __name__ == '__main__':
    update ()


# THE END
