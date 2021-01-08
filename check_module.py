

from bs4 import BeautifulSoup
import sys
import os
os.getcwd()

if os.name == 'nt':
    s = '\\'
else:
    s = '/'


def check_module(m):
    for path in sys.path:
        for candidate in [s.join([path, m+'.py']), s.join([path, m, '__init__.py'])]:
            if os.path.exists(candidate):
                print(candidate)
                return
    print(f'Module: {m} is not exist in {sys.path}')
    return

if __name__ == '__main__':
    if len(sys.argv) > 1:
        check_module(sys.argv[1])
    else:
        print(f'usage: python {sys.argv[0]} module')
