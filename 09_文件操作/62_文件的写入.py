# import time
#
# f = open('D:/ki7.txt','w',encoding='UTF-8')
# # write 写入
# f.write('时代少年团,我们喜欢你')
# # 刷新
# f.flush()
# 关闭   close()方法是内置了flush的功能的
# f.close()
# 打开一个存在的文件
f = open('D:/ki7.txt','w',encoding='UTF-8')
f.write("我们喜欢马嘉祺")
f.close()
# 如果打开的是不存在的文件 那么就创建 打开存在的文件 write就是覆盖