#記帳程式
products = []
p_sum = []
q_sum = []
while True:
	name = input('請輸入商品名稱:')
	if name == 'q':
		break
	price = input('請輸入商品價格')
	price = int(price)
	p = [name, price]
	q = [name, str(price)]
	products.append(p)
	q_sum.append(q)
	p_sum.append(price)
#print(products)

for product in products:
	print(product[0], '的價格是', product[1])

count = 0
for i in p_sum:
	count = count + i
print('今天一共消費金額為', count, '元')


with open('product.csv', 'w', encoding='utf-8') as f:#encoding='utf-8'為使用utf-8編碼
	f.write('商品,價格\n')#新增欄位名稱
	for q in q_sum:
		f.write(q[0] + ',' + q[1] + '\n')