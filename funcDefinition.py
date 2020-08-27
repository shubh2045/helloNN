def Perceptron(input1, input2, output):
    outputE = input1*weights[0]+input2*weights[1]+bias*weights[2]
    if outputE > 0:
        outputE = 1
    else:
        outputE = 0
    error = output-outputE
    weights[0] += error * input1 * lr
    weights[1] += error * input2 * lr
    weights[2] += error * bias * lr
