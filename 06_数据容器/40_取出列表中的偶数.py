my_list=[1,2,3,4,5,6,7,8,9,10]
# 遍历列表，取出列表中的偶数,并存入一个新的列表对象当中
index=0
my_list2=[]
while index<len(my_list):
    element=my_list[index]
    if element%2==0:
        my_list2.append(element)
    index+=1
print(my_list2)

my_list2=[]
k=my_list2
for element in my_list:
    if element%2==0:
        k.append(element)
print(k)



