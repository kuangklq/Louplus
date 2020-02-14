i = 0
while i < 100:
	i += 1
	if (i % 7 == 0) or ((i - 7) % 10 == 0) or (70 <= i <= 79):
		continue
	else:
		print(i)

