import requests
from pandas import DataFrame
import json
import plotly.graph_objects as go


def query_covid_data_api():
    url = "a5/product_status.json"
    res = requests.request("GET", url, headers=headers)
    res.raise_for_status()

    return res.json()


def generate_formatted_df(raw_data):
    df_formatted = DataFrame()

    store = []
    address = []
    bread = []
    steak = []
    ramen = []
    toliet_paper = []

    for i in range(len(raw_data)):
        store.append(raw_data.keys())
        address.append(raw_data[raw_data.keys()]["address"])
        bread.append(raw_data[raw_data.keys()]["bread"])
        steak.append(raw_data[raw_data.keys()]["steak"])
        ramen.append(raw_data[raw_data.keys()]["ramen"])
        toliet_paper.append(raw_data[raw_data.keys()]["toliet_paper"])

    df_formatted["store"] = store
    df_formatted["address"] = address
    df_formatted["bread"] = bread
    df_formatted["steak"] = steak
    df_formatted["ramen"] = ramen
    df_formatted["toliet_paper"] = toliet_paper

    return df_formatted


def generate_confirmed_plot(df_formatted):
    map_confirmed = go.Scattermapbox(
        store='store',
        address='address',
        bread='bread',
        steak='steak',
        toliet_paper='toliet_paper'
    )

    return map_confirmed


def generate_map(plots: list):
    layout = go.Layout(
        mapbox_style="white-bg",
        autosize=True,
        mapbox_layers=[
            {
                "below": 'traces',
                "sourcetype": "raster",
                "source": [
                    "http://mapbox://styles/mapbox/satellite-v9"
                ]
            }
        ])

    fig = go.Figure(data=plots, layout=layout)
    fig.update_layout(mapbox_style="open-street-map")
    fig.show()


def main():
    raw_data = query_covid_data_api()
    df = generate_formatted_df(raw_data=raw_data)
    print(df)
    plots = [generate_confirmed_plot(df=df)]
    generate_map(plots=plots)


if __name__ == "__main__":
    main()
