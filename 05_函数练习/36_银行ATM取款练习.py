money=5000000
name=None
name=input('请输入您的姓名：')

#定义主页面函数
def main():
    print(f'{name}您好,欢迎来到中国工商银行ATM,请选择操作：')
    print(f'查询余额\t[输入1]')
    print(f'存款\t\t[输入2]')
    print(f'退款\t\t[输入3]')
    print(f'退出\t\t[输入4]')
    return input('请输入您的选择：')
#定义查询余额的函数
def check_money(show_higher):
    if show_higher:
        print(f'----------查询余额-----------')
    print(f'{name}，您好,您的余额剩余{money}元')
#定义存款的函数
def save_money(num):
    global money
    money+=num
    print(f'----------存款---------------')
    print(f'{name},您好,您存款{num}元成功！')
    check_money(False)

#定义取款的函数
def take_money(num):
    global money
    money-=num
    print(f'-----------取款---------------')
    print(f'{name},您好，你取款{num}元成功！')
    check_money(False)

while True:
    keyboard_input=main()
    if keyboard_input == '1':
        check_money(True)
        continue
    elif keyboard_input == '2':
        num=int(input(f'您想要存入多少钱？请输入：'))
        save_money(num)
        continue
    elif keyboard_input == '3':
        num=int(input(f'您想要取出多少钱？请输入：'))
        take_money(num)
        continue
    else:
        print('您已退出ATM自助服务,很高兴为你服务！')
        break







