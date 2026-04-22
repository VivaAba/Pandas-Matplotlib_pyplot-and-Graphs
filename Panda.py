import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("exam_scores.csv")

# Bar Chart

# Horizontal
plt.figure(figsize=(8,5), num ="Plo Plo")
plt.barh(df["Student"],df["Mid Exam"], color ="Gray")
plt.xlabel("Student Names")
plt.ylabel("Student Scores")
plt.title("Mid Term Exam Scores")
plt.show()

# Lines
plt.figure(figsize=(8,5), num ="Plo Plo")
plt.plot(df["Student"],df["Mid Exam"], marker ="o", color ="Gray")
plt.xlabel("Student Names")
plt.ylabel("Student Scores")
plt.title("Mid Term Exam Scores")
plt.show()

# Normal
plt.figure(figsize=(8,5), num ="Plo Plo")
plt.bar(df["Student"],df["Mid Exam"], color ="Gray")
plt.xlabel("Student Names")
plt.ylabel("Student Scores")
plt.title("Mid Term Exam Scores")
plt.show()

# 1 Step : Show data frame entirely

# print(df)

# 2 Step : See the top 5.

# print(df.head())

# 3 Step : basic stats -min/max/avg

# print(df.describe())

# 4 Step : Grab Student names only

# print(df["Student"])

# 5 Step : Grab only Scores

# print(df["Mid Exam"])

# print("Mean", df["Mid Exam"].mean())
# print("Min", df["Mid Exam"].min())
# print("Max", df["Mid Exam"].max())

# # 6 Step : Grab student who got above 80
# print(df[df["Mid Exam"] > 80])