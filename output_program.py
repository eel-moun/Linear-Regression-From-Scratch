import pandas as pd
import json

def predict():
    with open("theta.json", "r") as f:
        params = json.load(f)
    theta0 = params["theta0"]
    theta1 = params["theta1"]

    df = pd.read_csv("data.csv")
    min_km = df["km"].min()
    max_km = df["km"].max()
    dif = max_km - min_km

    inp = input("Enter a km value: ")
    raw_km = 0

    if(inp.isnumeric()):
        raw_km = float(inp)
    else :
        print("bad input input should be a number")
        return 

    x_norm = (raw_km - min_km) / dif

    predicted_price = theta0 + theta1 * x_norm
    print(f"Predicted price for {raw_km} km: {predicted_price:.2f}")

if __name__ == "__main__":
    predict()