num=988
Sum=0
for k in range(num):
    if k%2==0:
        Sum+=1
print(f'num里一共有{Sum}个偶数')


f=0
for f in range(1,101):
    print(f'给小美表白的第{f}天......')
    for b in range(1,11):
        print(f'给小美送的第{b}朵玫瑰花')
    print('小美我喜欢你')
print(f'第{f}天，表白成功')


for i in range(1,101):
    j=1
    while j<=10:
        print(f'给小妹送的第{j}朵玫瑰花')
        j+=1
        print(f'小美我喜欢你')
    print(f'追小美的第{i}天。。。。。。')
print(f'表白成功')



