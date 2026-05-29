fr=open('D:/bill.txt','r',encoding='utf-8')
fw=open('D:/bill.txt.bak','w',encoding='utf-8')
for line in fr:
    line=line.strip()
    if line.split(',')[4]=='测试':
        continue
    fw.write(line)
    fw.write('\n')
# close两个文件
fr.close()
fw.close()



