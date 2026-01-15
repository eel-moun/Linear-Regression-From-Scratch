import pandas as pd
import matplotlib.pyplot as plt
import json
import numpy as np


def read_data(path):
    data = pd.read_csv(path)
    min_km = data['km'].min()
    max_km = data['km'].max()
    dif = max_km - min_km
    data["km"] = data["km"].apply(lambda x : ((x - min_km)/(dif)))
    return data


def gradient_descent( theta0, theta1, learning_rate, data):
    tmp_theta0 = 0
    tmp_theta1 = 0

    n = len(data)
    for i  in range(n):
        x = data.iloc[i].km
        y = data.iloc[i].price
        tmp_theta0 += learning_rate * (1/n) * ((theta0 + theta1 * x) - y)
        tmp_theta1 += learning_rate * (1/n) * ((theta0 + theta1 * x) - y) * x
    
    theta0 -= tmp_theta0
    theta1 -= tmp_theta1
    return theta0, theta1

def training():
    data = read_data("data.csv")
    theta0 = 0
    theta1 = 0
    learning_rate = 0.1
    epoch = 10000
    
    for i in range(epoch):
        theta0,theta1 = gradient_descent(theta0, theta1, learning_rate, data)

    result= {
        "theta0" : theta0,
        "theta1" : theta1
    }

    with open("theta.json", "w") as file:
        json.dump(result, file, indent=4)

    new_data = pd.read_csv("data.csv")
    min_km = new_data["km"].min()
    max_km = new_data["km"].max()
    dif = max_km - min_km
    
    plt.scatter(new_data.km, new_data.price)
    plt.savefig("points.png")
    x_values = np.arange(min_km, max_km, 25000)
    x_norm = (x_values - min_km) / dif
    y_values = theta0 + theta1 * x_norm

    plt.plot(x_values, y_values, color='red', label='Regression Line')
    plt.savefig("line.png")

training()
