from getssr import *

def get_wangzhan():
    url = 'http://ssr.wangzhan.gq/'
    http = request.urlopen(url)
    html = http.read().decode()
    ssrlist = re.findall(r'>ssr://.*?<',html)
    rlssr = [ssr.replace('<','') for ssr in[ssr.replace('>','') for ssr in ssrlist]]
    return rlssr