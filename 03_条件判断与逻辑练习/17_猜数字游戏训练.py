# 案例需求
# 定义一个数字1-10随机产生,通过三次判断来猜出数字
# 猜不中的话,提示猜大了还是猜小了
# 定义一个随机数变量
import random
num=random.randint(1,10)#随机数的范围为1-10
print('这是一个猜数字的小游戏，你一共有三次机会，猜的范围在1-10')
guess_num=int(input('请输入你要猜的数字'))
if guess_num==num:
    print('你也太厉害了，第一次就猜中了，答案为%d'%num)
else:
    if guess_num>num:
        print('你猜大了，你还有两次机会')
    else:print('你猜小了，你还有两次机会')
    guess_num=int(input('请输入你第二次猜的数字：'))
    if guess_num==num:
        print('恭喜你第二次就猜中了,答案为%d'%num)
    else:
        if guess_num>num:
            print('你猜大了，你还有一次机会')
        else:print('你猜小了,你还有一次机会')
        guess_num=int(input('请输入最后一次猜的数字'))
        if guess_num==num:
            print('恭喜你在最后一次机会猜对了,答案为%d'%num)
        else:
            if guess_num>num:
                print('你还是猜大了，正确答案为：%d'%num)
            else:print('你还是猜小了，正确答案为：%d'%num)
'''  错误缩进 有bug不知道问题在哪里
# 案例需求
# 定义一个数字1-10随机产生,通过三次判断来猜出数字
# 猜不中的话,提示猜大了还是猜小了
# 定义一个随机数变量
import random
num=random.randint(1,10)
# 通过if判断语句进行数字的猜测
print('这是一个猜数字的小游戏，你一共有三次机会，数字范围在1-10，看看你多久能猜中！')
guess_num=int(input('请输入你要猜测的数字：'))
if guess_num==num:
    print('恭喜你第一次就猜对了正确答案！答案是%d 太厉害了叭！'%guess_num)
else:
     if guess_num>num:
        print('你猜大了，你还有两次机会')
     else:
        print('你猜小了，你还有两次机会')
        guess_num = int(input('再次输入你要猜测的数字：'))
        if guess_num == num:
            print('恭喜你猜对了正确答案！答案是%d' % guess_num)
        else:
            if guess_num > num:
                print('你猜大了，你还有一次机会')
            else:
                print('你猜小了，你还有一次机会')
                guess_num = int(input('最后输入你要猜测的数字：'))
                if guess_num == num:
                    print('恭喜你猜对了正确答案！答案是%d' % guess_num)
                else:
                    if guess_num > num:
                        print('你还是猜大喽,正确答案是%d'%num)
                    else:
                        print('你还是猜小喽,正确答案是%d'%num)
#错误示例
uess_num = int(input('请输入你要猜测的数字'))
    if guess_num>num:
        print('猜大了哦！你还有一次机会！')
        guess_num = int(input('请输入你要猜测的数字'))
    elif guess_num < num:
        print('你猜小了哦！你还有一次机会！')
        guess_num = int(input('请输入你要猜测的数字'))
    else:print('恭喜你猜对了正确答案！答案是%d'%guess_num)
else:print('恭喜你第一次就猜对了正确答案！答案是%d 太厉害了叭！'%guess_num)
'''
