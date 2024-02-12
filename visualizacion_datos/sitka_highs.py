import csv
import matplotlib.pyplot as plt

filename = "data/sitka_weather_07-2018_simple.csv"
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    # print(header_row)

    # for index, column_header in enumerate(header_row):
    #     print(index, column_header)

    # Get max temperatures
    highs = []
    for row in reader:
        high = int(row[5])
        highs.append(high)

# print(highs)

fig, ax = plt.subplots()
ax.plot(highs, c='red')

plt.title("Daily max temperatures")
plt.xlabel("", fontsize=16)
plt.ylabel("Temperature", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()