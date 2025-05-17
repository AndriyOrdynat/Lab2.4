import matplotlib.pyplot as plt
import numpy as np
import pandas as pd 
import random

data = pd.DataFrame({
	'time': list(range(10)),
	'position': [i * random.uniform(1, 2) for i in range(10)],
    'speed': [None for _ in range(10)],
    'aceleration': [None for _ in range(10)]
})

data['speed'] = data['position'].diff() / data['time'].diff()
data['aceleration'] = data['speed'].diff() / data['time'].diff()

average_speed = data['speed'].mean()
average_aceleration = data['aceleration'].mean()
print(f"Average speed: {average_speed}")
print(f"Average aceleration: {average_aceleration}")

#plot 1:
plt.figure(figsize=(11, 3))
x = data['time']
y = data['position']

plt.subplot(1, 3, 1)
plt.plot(x, y, color='blue')
plt.title('x')
plt.xlabel('time')
plt.ylabel('position')

#plot 2:
x = data['time']
y = data['speed']

plt.subplot(1, 3, 2)
plt.plot(x, y, color='green')
plt.title('dx/dt')
plt.xlabel('time')
plt.ylabel('speed')

# plot 3:
x = data['time']
y = data['aceleration']

plt.subplot(1, 3, 3)
plt.plot(x, y, color='red')
plt.title('d²x/dt²')
plt.xlabel('time')
plt.ylabel('aceleration')

plt.tight_layout()
plt.show()