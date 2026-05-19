def list_while_func():
    mylist=[1,2,3,4,5,5,6,7,7,7,7,9,27]#通过while循环遍历list列表
    index=0
    while index<len(mylist):
        element=mylist[index]
        print(f'{element}')
        index+=1
# list_while_func()

def list_for_func():
    mylist=[1,2,3,4,5,5,6,7,7,7,7,9,27]
    for element in mylist:
        print(f'{element}')
list_for_func()
