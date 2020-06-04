#list exercise 2
numList = [81, 59, 32, 10, 12, 18]
mymax = numList[0]

for num in numList:
    if num > mymax:
        mymax = num

print(mymax)