#打开文件
# 读取文件 -read()
import time

f = open('D:/AI开发实习冲刺计划.txt','r',encoding='utf-8')
# print(f'读取一千个字节的结果是{f.read(1000)}')
# 读取文件 -readlines()
# lines=f.readlines()#读取文件的全部行，封装到列表
# print(f'lines对象的内容是{lines}')
# 读取文件-readline()
# line1=f.readline()
# line2=f.readline()
# line3=f.readline()
# line4=f.readline()
# print(f'第一行的数据：{line1}')
# print(f'第二行的数据：{line2}')
# print(f'第三行的数据：{line3}')
# print(f'第四行的数据：{line4}')

# for循环读取文件行
# for line in f:
#     print(f'每一行的数据是{line}')
#文件的关闭
# time.sleep(70000)
f.close()

# withopen()语法操作文件  操作完成之后 文件会自动close
with open('D:/AI开发实习冲刺计划.txt','r',encoding='utf-8') as f:
    for line in f:
        print(f'每一行的数据是{line}')