import sys
sys.path.append(".")

from envtest import my_calculate_mean

data = {
        'A': [1, 2, 3],
        'B': [4, 5, 6],
        'C': [7, 8, 9]
    }

mean_values = my_calculate_mean(data)
for column, mean in mean_values.items():
    print(f"{column}: {mean}")