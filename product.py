#記帳程式
products = []
p_sum = []
while True:
	name = input('請輸入商品名稱:')
	if name == 'q':
		break
	price = input('請輸入商品價格')
	price = int(price)
	p = [name, price]
	products.append(p)
	p_sum.append(price)
print(products)

for product in products:
	print(product[0], '的價格是', product[1])

count = 0
for i in p_sum:
	count = count + i
print('今天一共消費金額為', count, '元')