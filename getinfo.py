#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
第三步
'''
import requests
with open('href.txt','r',encoding='utf-8') as f:
    print(f.readline())
    r = requests.get(f.readline()) #仅仅获取一行作为测试
    print(r.status_code)
    print(r.text)
    with open('info.txt', 'w', encoding='utf-8') as i:
        i.write(r.text)


