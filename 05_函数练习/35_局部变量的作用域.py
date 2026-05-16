#定义全局变量
kiu=399
def test_b():
    #在函数内修改全局变量
    global kiu#在函数内修改全局变量
    kiu=889
    print(kiu)

def test_a():
    print(kiu)
'''print(num)
出了函数体局部变量 
'''
test_b()
test_a()
