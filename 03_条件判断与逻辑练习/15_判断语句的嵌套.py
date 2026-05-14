print('欢迎来到西安市国家森林游乐园！')
if int(input('请告诉我您的身高：   cm'))>=130:
    print('您的身高高于130cm需要买票入园！')
    print('不过您的vip等级大于4级也可以免费游玩哦！')
    if int(input('请告诉我您的vip等级： 级'))>=4:
        print('您的等级足够，可以免费入园！')
    else:print('sorry！您需要买票20元！')
else:print('您可以免费入园！祝您玩得开心！')


