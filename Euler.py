import numpy as np 
from matplotlib import pyplot as plt


def function(y):
	return y*(1-y**2)

def eulers(t0, y0, deltaT, s):
	currentS = 0
	y = y0
	while (currentS < s):
		y = deltaT*(y0*(1-y0**2))
		t0 = t0 + deltaT
		currentS =+ 1
		print ("t0 ", t0, "y ", y, "function ", function(y))

t0 = 0
y0 = -3
Y0 = 3
tf = 5
s = 101
deltaT = 0.05


x = np.linspace(t0, tf, s)
y = np.zeros([s])

for i in range(s):
	y0 += deltaT*(y0*(1-y0**2))
	y[i] = y0

X = np.linspace(t0, tf, s)
Y = np.zeros([s])
for i in range(s):
	Y0 += deltaT*(Y0*(1-Y0**2))
	Y[i] = Y0

for i in range(s):
	print(x[i],y[i])

plt.plot(x,y)
plt.plot(X,Y)
plt.xlabel("Value of x")
plt.ylabel("Value of y")
plt.title("Approximate solution using Euler's method")
plt.show()