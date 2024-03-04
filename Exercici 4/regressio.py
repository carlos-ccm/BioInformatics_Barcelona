import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


x = np.array([1,2,3,4,5,6,7,8,9,10]).reshape(-1,1)

media = 0
desviacion = 3
num_muestras = 10
ruido_gauss = np.random.normal(loc = media, scale = desviacion, size = num_muestras)

y = x * 5.5 +3 + ruido_gauss

from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(x,y)
#Aqui el model ja esta creat

# Fer prediccions
x_test = x
prediction = model.predict(x_test)
# print("Predicció:", prediction)


plt.scatter(x,y, label='dades', color='green')
plt.plot(x,prediction, label='predicció', color='blue')
plt.legend()
plt.show()


coeficientes = model.coef_
intercepto = model.intercept_


print("Coeficientes:", coeficientes)
print("Intercepto:", intercepto)