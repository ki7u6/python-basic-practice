#定义一个函数，名称任意，并接受一个参数传入，在函数内进行体温判断，正常范围是小于37.5
def health(tempreture=float(input('请出示您的健康码和您的体温'))):
    if tempreture<37.5:
        print(f'您的体温是{tempreture}度，体温正常请进')
    else:
        print(f'您的体温是{tempreture}度，需要隔离')
health()
