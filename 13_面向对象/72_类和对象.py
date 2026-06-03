# 设计一个闹钟类
class clock:
    id=None #序列号
    price=None #价格

    def ring(self):
        import winsound
        winsound.Beep(2000,3000)
# 构建两个闹钟对象并让其工作
clock1=clock()
clock1.id='003032'
clock1.price=100
clock1.ring()
print(f'闹钟ID：{clock1.id}，闹钟价格：{clock1.price}')
clock1.ring()

clock2=clock()
clock2.id='003033'
clock2.price=10000
clock2.ring()
print(f'闹钟ID：{clock2.id}，闹钟价格：{clock2.price}')
clock2.ring()