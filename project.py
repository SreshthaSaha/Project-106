import plotly_express as px
import csv
import numpy as np
import pandas as pd

def getDataSource(data_path):
    Sleep = []
    Coffee = []
    with open(data_path) as file:
        df = csv.DictReader(file)
        for row in df:
            Sleep.append(float(row["sleep in hours"]))
            Coffee.append(float(row["Coffee in ml"]))
    return {"x":Coffee,"y" :Sleep}

def findCorrelation(data_source):
    CorRelation = np.corrcoef(data_source["x"],data_source["y"])
    print("Co-Relation between amount of coffee drank and Average Sleep Time: ", CorRelation[0,1])

def plotFigure(data_path):    
    with open(data_path) as file:
        df = csv.DictReader(file)
        fig  = px.scatter(df,x = "Coffee in ml",y = "sleep in hours",color = "week")
        fig.show()

def setup():
    data_path = "Coffee_VS_Sleep.csv"
    DataSource = getDataSource(data_path)
    findCorrelation(DataSource)
    plotFigure(DataSource)

setup()