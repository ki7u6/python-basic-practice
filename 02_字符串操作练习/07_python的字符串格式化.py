name='小k'
dream='ai工程开发师'
salary=10086
message='面试者姓名%s,目标岗位是%s,期待薪资是%s元'%(name,dream,salary)
print(message)

name='小帅公司'
setup_year=1982
stock_price=999.99
message='需要上市的公司%s,公司成立的年份是%d,今日的股价是%f'%(name,setup_year,stock_price)
print(message)
# 没有控制精度

# 精度控制
num1=72
num2=39
num3=72.2739
message='num1宽度限制8,结果是%8d'%(num1)
print(message)
message='num2宽度限制3,结果是%3d'%(num2)
print(message)
message='num3宽度限制9,小数精度3，结果是%9.3f'%(num3)
print(message)

num4=11.8978
message='%10.1f'%(num4)
print(message)
num5=892
message='%4d'%(num5)
print(message)
num6=729.2728
message='%10.2f'%(num6)
num7=22
print(message)
message='%3d'%(num7)
print(message)

