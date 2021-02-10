import numpy as np
import pandas as pd


def get_rating_matrix(filename, dtype=np.float32):
    df = pd.read_csv(filename)
    return df.groupby(["source", "target"])["rating"].sum().unstack().fillna(0)
filename = "D:\\python-for-machine-learning\\2_Data_Handling\\assignment\lab_build_matrix\\movie_rating.csv"
df = pd.read_csv(filename)
df.groupby(["source", "target"])["rating"].sum()
get_rating_matrix(filename, np.float32)



def get_frequent_matrix(filename, dtype=np.float32):
    df = pd.read_csv(filename)
    df["rating"] = 1
    return df.groupby(["source", "target"])["rating"].sum().unstack().fillna(0)
filename = "D:\\python-for-machine-learning\\2_Data_Handling\\assignment\lab_build_matrix\\1000i.csv"
df = pd.read_csv(filename)
df["rating"] = 1
df
get_frequent_matrix(filename, np.float32)
