import matplotlib.pyplot as plt, mpld3
from random import random
import time

def plotTemperature():
	data = [random()]
	for i in range(100):
		data.append(random())
		plt.plot(data)
		plt.title('Temperature')
		plt.xlabel('Time')
		plt.ylabel('Temperature')
		plt.xlim(i-10,i)
		plt.pause(0.1)
		plt.clf()
	mpld3.show()

plotTemperature()