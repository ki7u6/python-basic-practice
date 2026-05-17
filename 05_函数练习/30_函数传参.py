#让用户随意输入两个数字，调用方法都可以算和
from unittest import result
def add(a=int(input('请输入a的值')),b=int(input('请输入b的值')),c=int(input('请输入c的值'))):
    return a+b+c
print(add())

def hhh(a,b,c):
    '''
    定义一个hhh函数可以求三个数之和
    :param a: 参数三数相加的第一个数
    :param b: 三数相加的第二个数
    :param c: 三数相加的第三个数
    :return: 返回resylt变量 接收三数之和
    '''
    result=a+b+c
    print(f'{a}+{b}+{c}最后的结果是{result}')
    return result
hhh(5,6,7)

