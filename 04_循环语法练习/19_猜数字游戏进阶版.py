# 设置一个范围1-100的随机整数变量，通过while循环，配合input语句，判断输入的数字是否为随机数
import random
num=random.randint(1,100)
#通过一个布尔类型的变量，做循环是否继续的标记
flag=True
court=0
while flag:
    guess_num=int(input('请输入你要猜的数字'))
    court+=1
    if guess_num==num:
        print(f'恭喜你第{court}次就猜中了正确答案%d'%num)
        flag=False
    else:
        if guess_num>num:
            print(f'抱歉，你第{court}次猜大了')
        else:
            print(f'抱歉，你第{court}次猜小了')


