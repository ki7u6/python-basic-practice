#定义一个函数，另一个函数作为参数传入
def user_info(ki7):
    result=ki7(7,7)
    print(f'ki7的参数类型是{type(result)}')
    print(f'内容是{result}')

#定义一个函数，作为参数传入另一个函数
def ki7(x,y):
    return x**y
user_info(ki7)

