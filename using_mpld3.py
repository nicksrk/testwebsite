import matplotlib.pyplot as plt, mpld3

plt.plot([3,1,4,1,5], 'ks-', mec='w', mew=5, ms=20)
plt.title('Temperature')
plt.xlabel('Time')
plt.ylabel('Temperature')
mpld3.show()