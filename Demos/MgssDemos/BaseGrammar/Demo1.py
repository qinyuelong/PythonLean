#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'''
https://github.com/mgss/python-demo
# Demo1：
# 有如下值集合 [11,22,33,44,55,66,77,88,99,90]，将所有大于 66 的值保存至字典的第一个key中，将小于 66 的值保存至第二个key的值中。
# 即： {'k1': 大于66的所有值, 'k2': 小于66的所有值}
'''



def test1():
    l = [11, 22, 33, 44, 55, 66, 77, 88, 99, 90]

    print(l)

    dic = {'k1': [i for i in l if i > 66],
           'k2': [i for i in l if i <= 66]
           }
    print(dic)



def test2():
    l = [11, 22, 33, 44, 55, 66, 77, 88, 99, 90]
    tup = {
        'k1' : [],
        'k2' : [],
    }

    for i in l:
        if i > 66:
            tup['k1'].append(i)
        else:
            tup['k2'].append(i)

    print(tup)




test1()
test2()