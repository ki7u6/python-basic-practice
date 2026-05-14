#print('告诉我你是谁')
aneeds=input('请告诉你要办理的银行业务？'
             '1.存钱'
             '2.取钱'
             '3.办理基金')
print('好的！接下来立刻为您办理%s业务！'%aneeds)
answer=input('请输入您的银行账号：')
answer=int(answer)
print('核对正确！您的银行账号%d正确！'%answer)

user_name=input('请输入您的姓名：')
user_age=input('请输入您的年龄：')
user_age=int(user_age)
user_type='ssssssvip用户！'
print(f'您好{user_name},您的年龄是{user_age}岁,您是我们尊贵的{user_type}')
print('您好%s,您的年龄是%d岁,您是我们最贵的%s'%(user_name,user_age,user_type))

