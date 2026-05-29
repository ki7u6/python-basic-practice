#通过from导入time中的sleep功能
from time import sleep as k
print('你好')
k(7)
print('不好')
# 使用*导入time模块的全部功能
from time import *
print('你好')
sleep(7)
print('不好')
# 使用as给特定功能加上别名
import time as ki7
print('你好')
ki7.sleep(7)
print('不好')