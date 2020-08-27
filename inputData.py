x = int(input())                                            #first input
y = int(input())                                            #second input
outputE = x*weights[0]+y*weights[1]+bias*weights[2]
if outputE > 0:
    outputE = 1
else:
    outputE = 0
print(x, "and", y, 'is: ', outputE )
