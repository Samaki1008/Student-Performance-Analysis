import pandas as pd
import matplotlib.pyplot as plt

# Load Data
df = pd.read_csv("../data/students.csv")
print(df.head())

# clean data

# 1) check nissig
print(df.isnull().sum())

# 2) Fill missing with mean
df["Math"] = df["Math"].fillna(df["Math"].mean())
df["Science"] = df["Science"].fillna(df["Science"].mean())
df["English"] = df["English"].fillna(df["English"].mean())

# Total Marks
df["Total"] = df["Math"] + df["Science"] + df["English"]


# Average Marks
df["Average"] = df["Total"] / 3
# print(df)

# Analysis
# Top students
print(df.sort_values(by="Total", ascending=False))

# City-wise Performance

print(df.groupby("City")["Average"].mean())

# Visualization
df.groupby("City")["Average"].mean().plot(kind="bar")
plt.title("Average Marks by City")
plt.show()
