f = open("data")

datatmp = f.read()

data = datatmp.split("\n\n")

count = 0

def findthing(string, thing):
	try:
		num = string.index(thing)
		text = string[num:].split(" ")[0]
		return text[0:].split("\n")[0]
	except:
		return False
def findValue(string):
	value = string.split(":")[1]
	return value

def checkbyr(value):
	if int(value) >= 1920 and int(value) <= 2002:
		return True
	else:
		return False

def checkiyr(value):
	if int(value) >= 2010 and int(value) <= 2020:
		return True
	else:
		return False

def checkeyr(value):
	if int(value) >= 2020 and int(value) <= 2030:
		return True
	else:
		return False

def checkhgt(value):
	if value[-2:] == "cm":
		if int(value[:-2]) >=150 and int(value[:-2]) <=193:
			return True
		else:
			return False
	if value[-2:] == "in":
		if int(value[:-2]) >= 59 and int(value[:-2]) <= 76:
			return True
		else:
			return False

def checkhcl(value):
	try:
		if value[-7] == "#":
			return True
		else:
			return False
	except IndexError:
		return False

def checkecl(value):
	if value == "amb" or value == "blu" or value == "brn" or value == "gry" or value == "grn" or value == "hzl" or value == "oth":
		return True
	else:
		return False

def checkpid(value):
	if len(value) == 9:
		return True
	else:
		return False


for passport in data:

	byr = findthing(passport, "byr")
	if byr == False:
		#print("passport not valid")
		continue

	iyr = findthing(passport, "iyr")
	if iyr == False:
		#print("passport not valid")
		continue

	eyr = findthing(passport, "eyr")
	if eyr == False:
		#print("passport not valid")
		continue

	hgt = findthing(passport, "hgt")
	if hgt == False:
		#print("passport not valid")
		continue

	hcl = findthing(passport, "hcl")
	if hcl == False:
		#print("passport not valid")
		continue

	ecl = findthing(passport, "ecl")
	if ecl == False:
		#print("passport not valid")
		continue

	pid = findthing(passport, "pid")
	if pid == False:
		#print("passport not valid")
		continue

	if checkbyr(findValue(byr)) != True:
		 continue
	if checkiyr(findValue(iyr)) != True:
		 continue
	if checkeyr(findValue(eyr)) != True:
		 continue
	if checkhgt(findValue(hgt)) != True:
		 continue
	if checkhcl(findValue(hcl)) != True:
		 continue
	if checkecl(findValue(ecl)) != True:
		continue
	if checkpid(findValue(pid)) != True:
		 continue
	else:
		count +=1
	


print(count)
