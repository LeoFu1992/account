#記帳程式
q_sum = []
import os #operating system
if os.path.isfile('product.csv'): #檢查檔案在不在
	print('找到檔案')
	with open('product.csv', 'r', encoding='utf-8') as f:
		for line in f:
			if '商品,價格' in line:
				continue #如果出現'商品,價格'就跳過此迴圈
			name, price = line.strip().split(',') #先將line裡面的分行符號去掉，在用split以 ,為界做切割
			q_sum.append([name, price,])
	#print(q_sum)
else:
	print('檔案已遺失....')
products = []
p_sum = []
while True:
	name = input('請輸入商品名稱:')
	if name == 'q':
		break
	price = input('請輸入商品價格')
	p = [name, int(price)]
	q = [name, price]
	products.append(p)
	q_sum.append(q)
	p_sum.append(int(price))
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
