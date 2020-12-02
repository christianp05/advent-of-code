f = open("data.txt", "r")

data = f.readlines()

for num1 in data:
	for num2 in data:
		for num3 in data:
			num4 = int(num2)+int(num1)+int(num3)
			if num4 == 2020:
				print(int(num1) *int(num2)*int(num3))
				break