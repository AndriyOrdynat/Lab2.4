import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('company_sales_data.csv')

df = pd.DataFrame(data)
df.set_index('month_number', inplace=True)
df.loc[:, ["facecream","facewash"]].plot.bar()
plt.title('Face Cream and Face Wash Sales Data')
plt.xlabel('Month Number')
plt.ylabel('Sales Units in number')
plt.xticks(rotation=0)
plt.grid(linestyle='--')
plt.legend(["Face Cream seles data", "Face Wash sales data"], loc='upper left')
plt.show()git 