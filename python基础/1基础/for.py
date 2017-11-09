#!/usr/bin/env python3
# -*- coding: utf-8 -*-


####### 循环 2017年10月30日

# for...in循环，依次把list或tuple中的每个元素迭代出来
names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)

# range函数
''' range(5)生成的序列是从0开始小于5的整数 '''
sum = 0
for x in range(101):
    sum = sum + x
print(sum)


''' #############################################课后练习
请利用循环依次对list中的每个名字打印出Hello, xxx!：
'''

L = ['Bart', 'Lisa', 'Adam']
for name in L:
    print("hello", name);
