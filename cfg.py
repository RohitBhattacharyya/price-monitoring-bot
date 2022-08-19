from configparser import ConfigParser
import os


cp = ConfigParser ()
cfgFile = os.path.join (os.path.dirname (os.path.abspath (__file__)), 'cfg.ini')


def make_cfg (filePath: os.path, section: str.lower, info: dict) -> None:
    cp.add_section (section)

    for key, value in info.items ():
        cp.set (section, key, value)

    with open (filePath, 'w') as f:
        cp.write (f)


def read_cfg (filePath: os.path, section: str.lower or None) -> dict:
    cp.read (filePath)

    inf = {}
    sec = cp.sections ()

    for s in sec:
        info = cp.items (s)
        inf [s] = info

    if section in inf:
        return inf [section]

    else:
        return inf


def update_cfg (filePath: os.path, section: str.lower, info: dict) -> None:
    cp.read (filePath)

    if section not in cp:
        cp.add_section (section)

    for key, value in info.items ():
        cp.set (section, key, value)

    with open (filePath, 'w') as f:
        cp.write (f)


if __name__ == '__main__':
    mode = input ('[1] Create\n[2] Read\n[3] Update\n[x] Exit\nEnter your choice: ')
    print ()

    if mode == '1':
        filePath = input ('Enter file path: ')
        section = input ('Enter section: ').lower ()
        info = {}
        numberOfKeys = int (input ('Enter number of keys: '))

        for i in range (numberOfKeys):
            key = input ('Enter key: ').lower ()
            value = input ('Enter value: ')
            info [key] = value

        if filePath == '':
            filePath = cfgFile

        if '.ini' not in filePath:
            filePath += '.ini'

        if section == '' or info == {}:
            print ('\033[91m' + '[ERROR] Invalid input' + '\033[0m')
            exit ()

        make_cfg (filePath, section, info)
        print ('\033[92m' + '[SUCCESS] Config file created' + '\033[0m')

    if mode == '2':
        filePath = input ('Enter file path: ')
        section = input ('Enter section: ').lower ()

        if filePath == '':
            filePath = cfgFile

        if '.ini' not in filePath:
            filePath += '.ini'

        if section == '':
            section = None

        info = read_cfg (filePath, section)

        print (f'\n{info}\n')

    if mode == '3':
        filePath = input ('Enter file path: ')
        section = input ('Enter section: ').lower ()
        info = {}
        numberOfKeys = int (input ('Enter number of keys: '))

        for i in range (numberOfKeys):
            key = input ('Enter key: ').lower ()
            value = input ('Enter value: ')
            info [key] = value

        if filePath == '':
            filePath = cfgFile

        if '.ini' not in filePath:
            filePath += '.ini'

        if section == '' or info == {}:
            print ('\033[91m' + '[ERROR] Invalid input' + '\033[0m')
            exit ()

        update_cfg (filePath, section, info)
        print ('\033[92m' + '[SUCCESS] Config file updated' + '\033[0m')

    if mode == 'x' or mode == 'X':
        exit ()