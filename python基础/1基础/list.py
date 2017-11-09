#!/usr/bin/env python3
# -*- coding: utf-8 -*-

####### list 2017年10月30日

##############################################

classmates = ['Michael', 'Bob', 'Tracy']
print(classmates);

# list的长度
print(len(classmates));

# 显示单个元素
print(classmates[-1]);
print(classmates[2]);

# 末尾插入
classmates.append('Adam')
print(classmates);

# 插入到指定地方
classmates.insert(1, 'Jack')
print(classmates);

# 删除List末尾
classmates.pop()
print(classmates);

# 把某个元素替换成别的元素
classmates[1] = 'Sarah'
print(classmates);

# list里面的元素的数据类型也可以不同


# 摘抄
L = list(range(100))