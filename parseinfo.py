#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
第四步
'''
import lxml.html
with open('info.txt','r',encoding='utf-8') as f:
    html = f.read()
    tree = lxml.html.fromstring(html)
    titles = tree.cssselect('.f20')[0].text_content()
    price = tree.cssselect('.house-basic-info .price')[0].text_content()
    huxing = tree.cssselect('.house-basic-info .room .main')[0].text_content()
    louceng = tree.cssselect('.house-basic-info .room .sub')[0].text_content()
    mianji = tree.cssselect('.house-basic-info .area .main')[0].text_content()
    maopi = tree.cssselect('.house-basic-info .area .sub')[0].text_content()
    phone = tree.cssselect('.phone-num')[0].text_content()
    print('标题：%s 价格：%s 户型：%s 楼层：%s 面积：%s 装修：%s 联系方式：%s '%(titles,price,huxing,louceng,mianji,maopi,phone))
