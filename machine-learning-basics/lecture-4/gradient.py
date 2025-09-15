import numpy as np

def gradient_d(x,y):
    m_curr = b_curr = 0
    iteratios = 1000
    n = len(x)
    for i in range(iteratios):
        y_pred = m_curr*x +b_curr
        


x = np.array[1,2,3,4,5]
y= np.array[4,6,8,10,12]

gradient_d(x,y)