# 定义变量
name='红星集团'
stock_price=19.99
stock_code='003032'
stock_price_daily_growth_factor=1.2
growth_day=7
print('公司：'+name,',股票代码：'+stock_code,',当前股价：'+str(stock_price))

#方法二
print(f'公司：{name},股票代码：{stock_code},当前股价：{stock_price}')
stock_price=stock_price*stock_price_daily_growth_factor**growth_day
print('每日增长系数是%.1f,'%stock_price_daily_growth_factor,'经过%d天的增长,'%growth_day,'股价达到了%.2f'%stock_price)

print('每日增长系数是%.1f,经过%d天的增长,股价达到了%.2f'%(stock_price_daily_growth_factor,growth_day,stock_price))