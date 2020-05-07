data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1    #count = count + 1
		if count % 1000 == 0:   # count 除以1000的餘數剛好為0才印
			print(len(data))

print('檔案讀取完了, 總共有', len(data), '筆資料')

print(data[0])   #印第一筆資料


sum_len = 0
for d in data:
	sum_len = sum_len + len(d)
	print(sum_len)

print('留言平均長度是', sum_len/len(data))

new = []
for d in data:  # for loop的意思就是把清單中的東西一個一個拿出來，d是字串 data 是清單
	if len(d) < 100:
		new.append(d)
print('一共有', len(new), '筆留言長度小於100')
print(new[0])
print(new[1])


good = []
for d in data:
	if 'good' in d:
		good.append(d)
print('一共有', len(good), '筆留言提到good')     


# Crtl + / 多行註解

#文字計數

wc = {}   # word_count 這本字典
for d in data:
	words = d.split()   #split的預設值就是用空白鍵來切割
	for word in words:
		if word in wc:
			wc[word] += 1    #在WC字典裏面查找word,如果那個字出現過,找到的字就會+1
		else:
			wc[word] = 1  #如果該字還沒出現過在word,就會新增key進字典

for word in wc:
	if wc [word] > 500000:
		print(word, wc[word])

print(len(wc))
print(wc['Allen'])    #查找allen這個字出現過幾次

while True:   #無限迴圈
	word = input('請問你想查什麼字: ')
	if word == 'q':
		break
	if word in wc:
		print(word, '出現過的次數為: ', wc[word])
	else:
		print('這個字沒有出現過喔!')

print('感謝使用本查詢功能')
