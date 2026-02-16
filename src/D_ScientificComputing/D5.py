import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from plotly.subplots import make_subplots

df = pd.read_csv("https://data.ub.uni-muenchen.de/2/1/miete03.asc", sep="\t")

def plot_NetRent(nm_sort):
    plt.figure(figsize=(10, 5))
    plt.plot(nm_sort, label="Prey (x)")
    plt.xlabel("Index")
    plt.ylabel("Net rent -nm")
    #plt.title("Lotka–Volterra Predator-Prey Simulation")
    #plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def plot_BoxPlot(data):
    fig = go.Figure()
    fig.add_trace(go.Box(y=data["nm"], name="Standard"))
    fig.add_trace(go.Box(y=data["nm"], name="With points", boxpoints="all"))
    fig.show()

def basicProperties(df: pd.DataFrame):
    nm_max = df['nm'].max()
    nm_min = df['nm'].min()
    nm_mean = df['nm'].mean()
    nm_median = df["nm"].median()
    nm_quartiles = df["nm"].quantile([1 / 4, 1 / 2, 3 / 4])

    return nm_max, nm_min, nm_mean, nm_median, nm_quartiles

def spread(df: pd.DataFrame, nm_quartiles):
    nm_var = df['nm'].var()
    nm_std = df["nm"].std()
    nm_IQR = nm_quartiles[0.75] - nm_quartiles[0.25]

    return nm_var, nm_std, nm_IQR

def plotHist(data):
    #----- rooms ------
    plt.hist(data["rooms"])
    plt.xlabel("rooms")
    plt.ylabel("# of rooms")
    plt.show()

    #----- year of building ------
    plt.hist(data["bj"])
    plt.xlabel("year of building")
    plt.ylabel("# of buildings")
    plt.show()

def correlation(data: pd.DataFrame):
    fig = make_subplots(rows=3, cols=1)

    fig.add_trace(go.Scatter(x=data["wfl"], y=data["nm"], mode="markers"), row=1, col=1)
    fig.update_xaxes(title_text="living area in m^2", row=1, col=1)
    fig.update_yaxes(title_text="net rent", row=1, col=1)

    fig.add_trace(go.Scatter(x=data["bj"], y=data["zh0"], mode="markers"), row=2, col=1)
    fig.update_xaxes(title_text="year of construction", row=2, col=1)
    fig.update_yaxes(title_text="central heating", row=2, col=1)

    fig.add_trace(go.Scatter(x=data["bj"], y=data["bez"], mode="markers"), row=3, col=1)
    fig.update_xaxes(title_text="year of construction", row=3, col=1)
    fig.update_yaxes(title_text="city district", row=3, col=1)

    fig.show()

def main() -> None:
    #----------------- 2.1 Basic properties of a data set ---------------------------
    nm_max, nm_min, nm_mean, nm_median, nm_quartiles = basicProperties(df)
    #print(f"{nm_max = }\n{nm_min = }\n{nm_mean = }\n{nm_median = }\n{nm_quartiles = }")
    #print(f"{nm_quartiles.keys() = }")

    #----------------- 2.1.1 Visualization -------------------------------
    nm_sort_val = df['nm'].sort_values()
    #plot_NetRent(nm_sort['nm'])
    #plot_BoxPlot(df)

    #-------------- 2.2 Spread -------------------------------
    nm_var, nm_std, nm_IQR = spread(df, nm_quartiles)
    #print(f"{nm_var = }\n{nm_std = }\n{nm_IQR = }")
   
    #------------------ 2.3 Histogram ------------------
    #plotHist(df)

    #------------ Correlation -------------
    correlation(df)
    

if __name__ == "__main__":
    main()