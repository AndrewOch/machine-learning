import random

import numpy as np
from matplotlib import pyplot as plt
from sklearn.svm import SVC


class Point:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color


colors = ["green", "blue"]


def create_dataset(num_points):
    dataset_train = []
    dataset_test = []
    for i in range(int(num_points / 2)):
        if i % 10 == 0:
            dataset_test.append(Point(random.randint(0, 50), random.randint(0, 50), 0))
        else:
            dataset_train.append(Point(random.randint(0, 50), random.randint(0, 50), 0))

    for i in range(int(num_points / 2)):
        if i % 10 == 0:
            dataset_test.append(Point(random.randint(55, 100), random.randint(55, 100), 1))
        else:
            dataset_train.append(Point(random.randint(55, 100), random.randint(55, 100), 1))

    for point in dataset_train:
        plt.scatter(point.x, point.y, color=colors[point.color])

    return dataset_train, dataset_test



def svm(train_points, test_points):
    train_data = [([point.x, point.y], point.color) for point in train_points]
    test_data = [([point.x, point.y], point.color) for point in test_points]

    train_x, train_y = zip(*train_data)
    test_x, test_y = zip(*test_data)

    model = SVC(kernel='rbf', C=1E6)
    model.fit(train_x, train_y)
    return model


def visualize_decision_boundary(svm_model, plot_ax=None):
    if plot_ax is None:
        plot_ax = plt.gca()
    x_limits = plot_ax.get_xlim()
    y_limits = plot_ax.get_ylim()

    x_vals = np.linspace(x_limits[0], x_limits[1], 30)
    y_vals = np.linspace(y_limits[0], y_limits[1], 30)

    grid_y, grid_x = np.meshgrid(y_vals, x_vals)
    grid_points = np.vstack([grid_x.ravel(), grid_y.ravel()]).T
    decision_values = svm_model.decision_function(grid_points).reshape(grid_x.shape)

    plot_ax.contour(grid_x, grid_y, decision_values, colors='black',
                    levels=[-1, 0, 1], alpha=0.7,
                    linestyles=['dotted', 'solid', 'dotted'])


if __name__ == "__main__":
    train_points, test_points = create_dataset(50)
    plt.savefig('result_1')

    model = svm(train_points, test_points)
    visualize_decision_boundary(model)
    plt.savefig('result_2')

    new_point = [60, 10]
    new_point_class = model.predict([new_point])[0]

    plt.scatter(new_point[0], new_point[1], color=colors[new_point_class])
    plt.savefig('result_3')
