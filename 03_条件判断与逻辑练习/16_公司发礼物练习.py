#  给公司员工发礼物
# 必须是大于十八岁小于三十岁的成年人
# 同时入职时间需满足大于两年，或者级别大于三才可以领取

age=int(input('请输入你的年龄：'))
work_year=int(input('请输入你的工龄：'))
work_leval=int(input('请输入你的工作级别：'))
# 开始判断
if age>=18:
    print("你已成年")
    if age<30:
        print('恭喜你满足工作年龄要求')
        if work_year>2:
            print('你的工龄和入职时长满足要求，你可以获得礼物')
        elif work_leval>3:
            print('你的工龄和工作级别满足要求，你可以获得礼物')
        else:print('抱歉，你不满足全部要求，请再接再厉！')
    else:print('抱歉，您的年龄太大不符合参与条件')

else:print('小朋友不可以参加哦！')
