#while循环的嵌套使用
# 外层表白一百天的控制
# 内层每天都送十朵玫瑰花的控制

day=1
while day<=100:
     print(f'今天是追小美第{day}天,准备表白。。。')
     day+=1
     many=1
     while many<=10:
         print(f'送给小美{many}朵玫瑰花')
         many+=1
     print('小美我喜欢你')
print(f'今天是追小美的{day-1}天,表白成功')
print(f'送了{many-1}朵,表白成功')




