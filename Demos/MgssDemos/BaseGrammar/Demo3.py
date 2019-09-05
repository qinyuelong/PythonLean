#!/usr/bin/env python3
# -*- coding:utf-8 -*-


'''
输出商品列表，用户输入序号，显示用户选中的商品
'''


# li = ["手机", "电脑", '鼠标垫', '游艇']
#
# for index, text in enumerate(li, 1):
#     print(index, text)


# inp = input('请选择您要购买的商品: ')
# try:
#     inp_num = int(inp)
#     print(li[inp_num - 1])
# except BaseException as e:
#     print(e)
#     print('输入不合法')



# def test2():
#     print('xx')
#
#
# def test(s):
#     print(s)

# test()
# test('aa')

from random import randint
def test(num):
   test = [1,2,3,4,5]
   print("ランダムで入力された数字は")
   print(test[num],"です")

num = randint(0,4)
test(num)