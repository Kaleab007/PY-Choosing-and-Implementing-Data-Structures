import numpy as np 
b = np.array([1,5,-2,10])

def array_sum(numberArr):
    arrSum = 0
    for i in numberArr:
        arrSUM = arrSUM + i
    return arrSUM
print(array_sum(b))

