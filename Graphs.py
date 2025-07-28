import matplotlib.pyplot as plt


def histogram_len_functions(lengths):
    plt.hist(lengths, bins=range(0, max(lengths) + 5, 1), edgecolor='black')
    plt.xticks(range(max(lengths) + 6))
    plt.title("Distribution of function lengths")
    plt.xlabel("Lines number")
    plt.ylabel("Functions number")
    plt.grid(True)
    plt.show()


def plot_pie_chart(labels, sizes):
    if len(labels) != len(sizes):
        raise ValueError("The length of 'labels' and 'sizes' must be the same.")
    colors = plt.cm.tab20.colors[:len(labels)]
    fig, ax = plt.subplots(figsize=(8, 8))
    wedges, texts, autotexts = ax.pie(
        sizes,
        labels=labels,
        colors=colors,
        autopct='%1.1f%%',
        startangle=90,
        textprops={'fontsize': 12}
    )
    ax.axis('equal')
    plt.title("Pie Chart", fontsize=16)
    plt.tight_layout()
    plt.show()

def plot_bar_chart(labels, values):
    if len(labels) != len(values):
        raise ValueError("The length of 'labels' and 'values' must be the same.")
    fig, ax = plt.subplots(figsize=(10, 6))
    bars = ax.bar(labels, values, color=plt.cm.tab20.colors[:len(labels)])
    ax.set_xlabel('Labels', fontsize=14)
    ax.set_ylabel('Values', fontsize=14)
    ax.set_title('Bar Chart', fontsize=16)
    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'{height}',
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom', fontsize=12)
    plt.tight_layout()
    plt.show()


# histogram_len_functions([3, 3, 3, 3, 3, 3, 3, 8, 6, 10, 15, 8, 4])
labels = ['תפוחים', 'בננות', 'תפוזים', 'ענבים']
sizes = [25, 30, 20, 25]

# plot_pie_chart(labels, sizes)

labels = ['A', 'B', 'C', 'D']
values = [10, 24, 36, 18]

plot_bar_chart(labels, values)
