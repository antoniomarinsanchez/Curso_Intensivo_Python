import matplotlib.pyplot as plt

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
# Colors test
# ax.scatter(x_values, y_values, c='red', s=10)
# ax.scatter(x_values, y_values, c=(0, 0.8, 0), s=10)
ax.scatter(x_values, y_values, c=y_values,cmap=plt.cm.Blues, s=10)

ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Values", fontsize=14)
ax.set_ylabel("Square values", fontsize=14)

ax.tick_params(axis='both', which='major', labelsize=14)
ax.axis([0, 1100, 0, 1100000])

plt.show()
# Save the figure
# plt.savefig('squares_plot.png', bbox_inches='tight')