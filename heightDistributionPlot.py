import pandas as pd
import plotly.figure_factory as pf

df = pd.read_csv("data.csv")
fig = pf.create_distplot([df["Height(Inches)"].tolist()], ['Height in Inches'], show_hist = False)
fig.show()