import pandas as pd
import plotly.figure_factory as pf

df = pd.read_csv("data.csv")
fig = pf.create_distplot([df["Weight(Pounds)"].tolist()], ["Weight in Pounds"], show_hist=False)
fig.show()