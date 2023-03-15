import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

customers = pd.read_csv("E-commerce Customers")

customers.head()
customers.describe()
customers.info()


sns.set_palette("GnBu_d")
sns.set_style('whitegrid')
sns.jointplot(x='Time on Website',y='Yearly Amount Spent',data=customers)

sns.jointplot(x='Time on App',y='Yearly Amount Spent',data=customers)
