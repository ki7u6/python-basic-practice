# 员工编号为1-20,从编号1开始领,依次领取,每人可以领取1000元
# 领工资时,财务判断员工的绩效分,随机生成,如果低于5则不发工资，换下一位
# 如果发完了,结束发工资
import random
work_money=10000
for k in range(1,21):
    num=random.randint(1,10)
    if work_money==0:
        print('工资发完了，下个月领取吧！')
        break
    else:
        if num>=5:
            work_money-=1000
            print(f'向员工{k}发放工资1000元，账户余额还剩{work_money}元')
        else:
            print(f'员工{k},绩效分{num},低于5，不发工资，下一位。')
            continue



money=10000
import random
for k in range(1,21):
    num=random.randint(1,10)
    if num<5:
        print(f'员工{k},绩效分{num},低于5，不发工资，下一位。')
        continue
    if money>=1000:
        money-=1000
        print(f'向员工{k}发放工资1000元，账户余额还剩{money}元')
    else:
        print('工资发完了，下个月领取吧！')
        break

money=10000
import random
for k in range(1,21):
    num=random.randint(1,10)
    if num>=5:
        if money>=1000:
            money-=1000
            print(f'向员工{k}发放工资1000元，账户余额还有{money}元')
            continue
        else:
            print('工资发完了，下个月领取吧！')
            break
    else:
        print(f'员工{k},绩效分{num},低于5，不发工资，下一位。')













