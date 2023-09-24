import pandas as pd


def task1(data):
    print(data[(data.Embarked == "S") & (data.Pclass == 1)].shape[0])


def task2(data):
    print(data[(data.SibSp > 1) & (data.Pclass == 3)].shape[0])


def task3(data):
    p = data[(data.Pclass == 1)]
    m = p.Fare.mean()
    print(m)


if __name__ == "__main__":
    data = pd.read_csv("/mix/train.csv")
    print(data[data.Sex == "female"].shape[0])
    print(data[(data.Sex == "female") & (data.Age < 18)].shape[0])
    task1(data)
    task2(data)
    task3(data)
    data['Family'] = data["SibSp"] + data["Parch"]
