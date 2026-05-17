money=5000000
name=None
name=input('请输入您的姓名：')
#定义查询函数
def check_money(show_header):
    if show_header:
        print('------查询余额------')
    print(f'{name},您好,您的余额剩余{check_money()}元')
#定义存款函数
def save_money(num):
    global money
    money+=num
    print('------存款--------')
    print(f'{name},您好，您存款{num}元成功')

    #调用save_money查询余额
    save_money(False)

def take_money(num):
    global money
    money-=num
    print('------取款--------')
    print(f'{name},您好,您取款{num}元成功')
    # 调用take_money查询取款
    take_money(False)

    #定义主菜单函数
def main():
        print('------主菜单------')
        print(f'{name},欢迎来到工商银行ATM,请完成你的操作：')
        print('查询余额\t[输入1]')
        print('存款\t\t[输入2]')
        print('取款\t\t[输入3]')
        print('退款\t\t[输入4]')
        print('-----------------')
        return print('请输入您的选择：')

    #设置无限循环，确保程序不退出

while True:
    keyboard_input=main()
    if keyboard_input == '1':
        check_money(True)
        continue # 通过continue进行下一次循环，一进来就是回到了主菜单
    elif keyboard_input == '2':
         num=int(input(f'您想要存入多少钱？请输入：'))
         save_money(num)
         continue
    elif keyboard_input == '3':
         num=int(input(f'您想要取出多少钱？请输入：'))
         take_money(num)
         continue
    else:
        print('程序退出啦！')
        break






















