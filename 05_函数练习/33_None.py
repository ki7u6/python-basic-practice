#定义一个检查是否成年的函数
def check_age(age):
    if age>=18:
        return 'success'
    else:
        return None
result=check_age(17)
if not result :
    print('未成年不可以进入网吧')
else:
    print('已成年，可以进入网吧')



