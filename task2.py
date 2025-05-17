import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_excel("voltage.xlsx")

Ohmic_conductivity = plt.figure()
plt.plot(data.loc[:, 'Voltage_1 (1)'], data.loc[:, 'abs(col(Current11))'])
plt.yscale('log')
plt.title('Омічна провідність')
plt.xlabel('Voltage_1 (1)')
plt.ylabel('abs(col(Current11))')


injection_conductivity = plt.figure()
plt.plot(data.loc[:, 'col(Iabs)/col(Uabs)'], data.loc[:, '1/col(Uabs)'])
plt.yscale('log')
plt.title('Інжекційна провідність')
plt.xlabel('col(Iabs)/col(Uabs)')
plt.ylabel('1/col(Uabs)')


Fowler_Nordheim_conductivity = plt.figure()
plt.plot(data.loc[:, 'col(Iabs)/col(Uabs)^2'], data.loc[:, '1/col(Uabs)'])
plt.yscale('log')
plt.title('Провідність за Фаулера-Нордгеймом')
plt.xlabel('col(Iabs)/col(Uabs)^2')
plt.ylabel('1/col(Uabs)')

Poole_Frenkel_conductivity = plt.figure()
plt.plot(data.loc[:, 'col(Iabs)/col(Uabs)'], data.loc[:, 'col(Uabs)^0.5'])
plt.yscale('log')
plt.title('Провідність Пула-Френкеля')
plt.xlabel('col(Iabs)/col(Uabs)')
plt.ylabel('col(Uabs)^0.5')

# plt.show()
U = data.loc[:, '1/col(Uabs)']
I = data.loc[:, 'col(Iabs)/col(Uabs)']

print(f"MAX: U = {1/U.min()} \n     I = {max(I/U)} \n")
print(f"MIN: U = {1/U.max()} \n     I = {min(I/U)} \n")