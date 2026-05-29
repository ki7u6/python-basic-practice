def func1():
    print('从fun1开始')
    1/0
    print('从fun1结束')
def func2():
    print('从fun2开始')
    func1()
    print('从fun2结束')
def main():
    try:
        func2()
    except Exception as e:
        print(f'出现异常了，异常的信息是{e}')
main()