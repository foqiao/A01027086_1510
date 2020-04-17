from a5.extra_project import generate_formatted_df
import numpy as np
import matplotlib.pyplot as plt

def plot():
    country = df_formatted['country']
    death = df_formatted['death']
    for i in country:
        for j in death:
            ax = plt.subplots()
            ax.barh(i, j)
            ax.set_xlabel(country)
            ax.set_ylabel(num)
            for k in range(0, 91):
                num = k * (10 ** 6)