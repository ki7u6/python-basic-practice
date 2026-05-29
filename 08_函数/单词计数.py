f=open('D:/word.txt','r',encoding='utf-8')
# 读取全部 挨个查找
# content=f.read()
# count=content.count('ki7')
# print(f'ki7的单词一共在word.txt中一共有{count}次')

# 一行一行读取
count=0
for line in f:
    line=line.strip()#取出收尾空格 以及换行符
    count+=line.count('ki7') #统计当前行的ki7数量，累加到count
print(f'ki7的单词一共在word.txt中一共有{count}次')
