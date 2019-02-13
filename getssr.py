from urllib import request
import re
from getssrfunc import *

def txt(ssrlist):
        with open('ssr.txt','w') as f:
                for ssr in ssrlist:
                        f.write(ssr+'\n')

def main():
        ssrlist = get_wangzhan()
        txt(ssrlist)

if __name__ == '__main__':
        main()
