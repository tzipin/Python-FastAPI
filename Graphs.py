import matplotlib.pyplot as plt


def histogram_len_functions(lengths):
    plt.hist(lengths, bins=range(0, max(lengths)+5, 1), edgecolor='black')
    plt.xticks(range(max(lengths)+6))
    plt.title("Distribution of function lengths")
    plt.xlabel("Lines number")
    plt.ylabel("Functions number")
    plt.grid(True)
    plt.show()


histogram_len_functions([3, 3, 3, 3, 3, 3, 3, 8, 6, 10, 15, 8, 4])
