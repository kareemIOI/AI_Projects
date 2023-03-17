import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('HeightWeightDataSet.csv')



def gradint_decent(m_now, b_now, points, L):
    m_gradient = 0
    b_gradient = 0
    
    n = len(points)
    
    for i in range(n):
        x = points.iloc[i].Height
        y = points.iloc[i].Weight
        m_gradient += -(2/n) * x * (y - (m_now * x + b_now))
        b_gradient += -(2/n) * (y-(m_now * x + b_now))
        
    m = m_now - m_gradient * L
    b = b_now - b_gradient * L
    return m, b


m = 0
b = 0
L = 0.0001
epoches = 100

for i in range(epoches):
    if i % 50 == 0:
        print(f"epoch: {i}")
    m, b = gradint_decent(m, b, data, L)
    
print(m, b)
plt.scatter(data.Height, data.Weight, color = "black")

plt.plot(list(range(60, 98)), [m * x + b for x in range(60, 98)], color = "red")

plt.show()
