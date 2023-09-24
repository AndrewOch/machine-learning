import pandas as pd
import matplotlib.pyplot as plt

file = "Sunspots.csv"


def rolling_mean(y):
    n = 25
    result = y.rolling(window=n).mean()
    plt.plot(result, color="r")


def exponential(y):
    alpha = 0.5
    result = [y[0]]
    for i in range(1, len(y)):
        result.append(alpha * y[i] + (1 - alpha) * y[i - 1])
    plt.plot(result, color="g")


def dataset(filename):
    data = pd.read_csv(filename)
    return data['Date'], data[data.columns[2]]


def draw(x, y):
    plt.figure(figsize=(40, 10))
    plt.scatter(x, y)
    rolling_mean(y)
    exponential(y)
    plt.show()


if __name__ == "__main__":
    date, sunspots = dataset(file)
    draw(date, sunspots)
