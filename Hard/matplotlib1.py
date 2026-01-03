import matplotlib.pyplot as plt

plt.plot([1,2,3], [4,5,6])
plt.show()

plt.bar(["A", "B", "C"], [10, 20, 15])
plt.show()

students = [1,2,3,4,5]
marks = [60,70,80,75,90]

plt.plot(students, marks, marker='o')
plt.xlabel("Students")
plt.ylabel("Marks")
plt.title("Student Performance")
plt.show()



