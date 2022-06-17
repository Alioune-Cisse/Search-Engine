# -*- coding: utf-8 -*-
"""
Created on Mon Jun  6 18:27:57 2022

@author: lenovo
"""
from EN import EN
import pandas as pd

df = EN()

def search(elt, df=df):
    data = []
    for i in range(len(df['Contenus'])):
        if(elt.lower() in df.Contenus[i].lower() and elt!=""):
            #data.append(df.Contenus[i][:100])
            values = {}
            values["Titre"] = df.Titre[i]
            values["Contenus"] = df.Contenus[i]
            values["Source"] = df.Source[i]
            values["Date Publication"] = df["Date Publication"][i]
            data.append(values)
    return pd.DataFrame(data)