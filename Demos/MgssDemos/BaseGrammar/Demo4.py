#!/usr/bin/env python3
# -*- coding:utf-8 -*-


'''

要求用户输入总资产，例如：2000
显示商品列表，让用户根据序号选择商品，加入购物车
购买，如果商品总额大于总资产，提示账户余额不足，否则，购买成功。
附加：可充值、某商品移除购物车

'''


goods = [
    {"name": "电脑", "price": 1999},
    {"name": "鼠标", "price": 10},
    {"name": "游艇", "price": 20},
    {"name": "美女", "price": 998},
]

print(goods)


total_money = 0.0


# 充值
def recharge():
    global total_money
    t = input('请输入充值金额: ')
    try:
        money = float(t)
        total_money += money
        print(total_money)

        d = globals()
        print(d)
        d['total_money'] = 100
        print(d)
        print(globals())

        print('\n')

        l = locals()
        print(l)
        l['t'] = 40
        b = 3
        l['b'] = 5

        print(l)
        print(locals())
    except BaseException as e:
        pass




recharge()



def a():
    b=1
    c=locals()
    print(c)
    b=2
    print (' 1. ', locals())
    print(c)
    c['b']=3
    print (' 2. ', locals())
    print (b)
    locals()['b']=3
    print (' 3. ', locals())
    print (b)
    print (c)


# a()