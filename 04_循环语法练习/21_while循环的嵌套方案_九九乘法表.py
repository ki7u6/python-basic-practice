k=1# 对应的是行
while k<=9:
    m=1# 对应的是列
    while m<=k:
        print(f'{m}*{k}={k*m}\t',end='')
        m+=1
    k+=1
    print()

