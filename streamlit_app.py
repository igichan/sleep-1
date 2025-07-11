import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.plot(x, y, marker='o')
plt.title("간단한 선 그래프")
plt.xlabel("X 축")
plt.ylabel("Y 축")
plt.show()
