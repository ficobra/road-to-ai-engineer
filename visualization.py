import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

data = pd.read_csv("output.csv")

x = data["name"]
y = data["salary"]
plt.plot(x, y)
plt.title("Salary values for each person")
plt.xlabel("Name")
plt.ylabel("Salary")
plt.savefig("line_chart.png")
plt.clf()

y = data["age"]
plt.bar(x, y)
plt.title("Age of each person")
plt.xlabel("Name")
plt.ylabel("Age")
plt.savefig("bar_chart.png")
plt.clf()

sns.histplot(data["salary"])
plt.title("Distribution of Salary")
plt.xlabel("Salary")
plt.ylabel("Num")
plt.savefig("histogram.png")
plt.clf()

x = data["salary"]
plt.scatter(x, y)
plt.title("Scatter Plot for Age vs Salary")
plt.xlabel("Salary")
plt.ylabel("Age")
plt.savefig("scatter_plot.png")
plt.clf()

correlation = data.corr(numeric_only=True)
sns.heatmap(correlation, annot=True, fmt=".2f")
plt.title("Correlation Heatmap")
plt.savefig("heatmap.png")
plt.clf()