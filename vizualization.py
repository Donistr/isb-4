import matplotlib.pyplot as plt


def visualize_statistic(statistic: dict) -> None:
    """
    function builds and draw a bar chart based on the statistic
    :param statistic: statistic
    :return: None
    """
    plt.figure(figsize=(30, 5))
    plt.ylabel('time')
    plt.xlabel('cores')
    plt.title('Brute statistic')
    x = statistic.keys()
    y = statistic.values()
    plt.bar(x, y, color='gold', width=0.05)
    plt.show()
