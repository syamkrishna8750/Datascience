import matplotlib.pyplot as plt

marks = [22, 87, 5, 43, 56, 73, 55, 54, 11, 20, 51, 5, 79, 31, 27]

bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

plt.hist(marks, bins=bins, edgecolor="red")

plt.xlabel("Marks Range")
plt.ylabel("Number of Students")
plt.title("Histogram of Student Marks")

plt.show()

