#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
TODO 第二步
'''
import lxml.html
with open('b.txt','r',encoding='utf-8') as f:
    html = f.read()

    tree = lxml.html.fromstring(html)
    titles = tree.cssselect('.title a')
    with open('href.txt', 'w+', encoding='utf-8') as h:
        for i in titles:
            print(i.get('href'))
            h.write(i.get('href')+'\n')