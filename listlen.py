a = [1,3,5,7,9]
for i in range(0, len(a)):
	print(a[i]*a[i])
	a[i] = a[i]*a[i]
print(a)	