# #基本捕获语法
# try:
#     f=open('D:/abc.txt','r',encoding='utf-8')
# except:
#     print(f'出现异常了，因为文件不存在，我要将open的模式改为w模式去运行')
#     f=open('D:/abc.txt','w',encoding='utf-8')
#
# # 捕获指定的异常
# try:
#     print(name)
#     # 1/0
# except NameError as e:
#     print(f'出现了变量未定义的异常')
#     print(e)
#     # 捕获多个异常
# try:
#     1/0
#     print(name)
# except(NameError,ZeroDivisionError) as e:
#     print('出现了未定义或者除以0的异常错误')
#     print(e)

    # 捕获所有异常
try:
     f=open('D:/1234567.txt','r',encoding='utf-8')
except Exception as e:
    f=open('D:/1234567.txt','w',encoding='utf-8')
    print('出现异常了,要把r换成w')
    print(e)
else:
    print('好高兴，没有异常')
finally:
    print(f'我是finally，有没有异常我都要执行')
    f.close()