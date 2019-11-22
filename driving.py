country = input('請問你是哪國人：')
age = input('請問你幾歲：')
age = int(age)
if country == '台灣':
	if age >= 18:
		print('你可以考駕照')
	else: 
		print('你還不可以考駕照')
elif country == '美國':
	if age >= 16:
		print('你可以考駕照')
	else:
		print('你還不可以考駕照')
else:
	print('本程式只限定應用於台灣或美國，請重新輸入')

