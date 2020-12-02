f = open("data", "r")

data = f.readlines()

bigCount = 0

for line in data:
	splitText = line.split("-")
	splitText2 =  splitText[1].split(" ")
	first = splitText[0]
	second = splitText2[0]
	letter =  splitText2[1][0]
	count = 0
	if splitText2[2][int(second)-1] == letter and splitText2[2][int(first)-1] != letter:
		bigCount +=1
	if splitText2[2][int(second)-1] != letter and splitText2[2][int(first)-1] == letter:
		bigCount +=1
print(bigCount)
