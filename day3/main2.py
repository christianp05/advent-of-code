f = open("data", "r")

leng = 31

data = f.readlines()


def getTrees(xIncrement, yIncrement):
        count = 0
        x = 0
        y = 0
        while True:
                try:
                        if data[y][x] == "#":
                                count +=1
                        x += xIncrement
                        y += yIncrement

                        if x >= leng:
                                offset = x - leng
                                x = offset
                except:
                        break
        return count




count1 = getTrees(1,1)
count2 = getTrees(3,1)
count3 = getTrees(5,1)
count4 = getTrees(7,1)
count5 = getTrees(1,2)


print("Part 1 answer: ", count2)
print("Part 2 answer: ", count1*count2*count3*count4*count5)