#!/usr/local/bin/python
__version__ = '0.1'

HOME_URL = 'https://raw.githubusercontent.com/ftobia/longshot/develop/longshot.py'


def upgrade():
    backup_self()
    download_and_overwrite()
    restart()


def backup_self():
    import shutil
    new_name = __file__ + '.bak'
    shutil.copy(__file__, new_name)


def download_and_overwrite():
    import urllib2
    response = urllib2.urlopen(HOME_URL)
    with open(__file__, 'w') as f:
        f.write(response.read())


def restart():
    import os, sys
    os.execvp(sys.executable, [sys.executable] + sys.argv)


if __name__ == '__main__':
    import sys
    print sys.executable
    print sys.argv
    print __version__
    upgrade()
