#定义一个函数，接受其他函数输入
def user_info(tumple):
    rusult=tumple(7,2)
    print(f'resulet:{rusult}')
# 通过lambda匿名函数的形式，将匿名函数作为参数传入
user_info(lambda x,y:x**y)
