#Lists exercise 9
# x = [[2, -2], [5, 3]]

# for i in range(len(x)) :
#     for j in range(len(x[i]) :
#         y = x[i] + x[j]
    
# print(y)

# outsideIndex = 0
# innerIndex = 0

# while outsideIndex < len(x) :
#     while innerIndex < len(x[outsideIndex]) :
#         output = x[outsideIndex][innerIndex]
#         print(f"{output}")
#         innerIndex += 1
#     innerIndex = 0
#     outsideIndex += 1

a = [ [2, -2],  
    [ 5, 3 ] ]  
i = 0
j = 0
while i < len(a) :  
    while j < len(a[i]) :  
        sumNum = a[i] + a[j]
        print(sumNum)
    