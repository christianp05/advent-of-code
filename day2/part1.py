f = open("data", "r")

data = f.readlines()

bigCount = 0

for line in data:
	splitText = line.split("-")
	splitText2 =  splitText[1].split(" ")
	min = splitText[0]
	max = splitText2[0]
	letter =  splitText2[1][0]
	count = 0
	for char in splitText2[2]:
		if char == letter:
			count += 1
	if count <= int(max) and count >= int(min):
		bigCount += 1
print(bigCount)
