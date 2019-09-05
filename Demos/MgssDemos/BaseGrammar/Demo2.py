#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'''

查找列表中元素，移除每个元素的空格，并查找以 a或A开头 并且以 c 结尾的所有元素。

'''



def findAndReplaceData():
    li = ["alec", " aric", "Alex", "Tony", "rain"]
    tu = ("alec", " aric", "Alex", "Tony", "rain")
    dic = {'k1': "alex", 'k2': ' aric', "k3": "Alex", "k4": "Tony"}

    tump = []
    temp_u = list(tu)

    for i in range(0, len(li)):
        # 去除空格
        li[i] = li[i].strip()

        # 以a A 开头 或者 c 结尾
        if li[i].endswith('c') and li[i].capitalize().startswith('A'):
            tump.append(li[i])

    print(tump)

    for i in range(0, len(temp_u)):
        temp_u[i] = temp_u[i].strip()
        if temp_u[i].endswith('c') and temp_u[i].capitalize().startswith('A'):
            tump.append(temp_u[i])

    print(tump)

    for item in dic.values():
        item = item.strip()
        if item.endswith('c') and item.capitalize().startswith('A'):
            tump.append(item)



    print(tump)


findAndReplaceData()

