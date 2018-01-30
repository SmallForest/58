#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
TODO 第一步
'''
import requests
r = requests.get('http://jn.58.com/ershoufang/0/?PGTID=0d300000-0000-06be-d278-c5f8302490b6&ClickID=1')
print(r.status_code)
print(r.text)
with open('b.txt','w',encoding='utf-8') as f:
    f.write(r.text)