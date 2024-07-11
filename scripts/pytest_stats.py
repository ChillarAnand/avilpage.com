import matplotlib.pyplot as plt
import numpy as np

# Data
groups = ['1', '2', '3', '4']
tests = [875, 497, 359, 337]
total = [1324, 918, 668, 548]
coverage = np.subtract(total, tests)
print(coverage)

fig, ax = plt.subplots()

# Stacked bar chart
ax.bar(groups, tests, label="Tests")
ax.bar(groups, coverage, bottom=tests, label="Coverage")

# Labels
for bar in ax.patches:
    ax.text(bar.get_x() + bar.get_width() / 2,
            bar.get_height() / 2 + bar.get_y(),
            round(bar.get_height()), ha='center',
            color='w', weight='bold', size=8)

for i, total in enumerate(total):
    ax.text(i, total + 1.0, round(total),
            ha='center', weight='bold', color='black')

ax.legend()
ax.set_ylabel('Duration (Seconds)')
ax.set_xlabel('Number of CPUs')

plt.show()
