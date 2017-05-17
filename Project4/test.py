while True:
	print("Nhap so nguyen tu 30-300")
	dl=input()
	x=int(dl)
	if x<=300 and x>=30:
		break
if x%7==0:
	if x%13==0:
		for i in range(97,123):
			ch=chr(i)
			print(ch)
	else:
		print ("abc")
elif x%13==0:
	print("xyz")


