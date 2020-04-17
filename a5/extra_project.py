import requests
import geojson
from pandas import DataFrame
import json
import plotly.graph_objects as go


def query_covid_data_api():
    # https://rapidapi.com/ShubhGupta/api/covid19-data?endpoint=apiendpoint_c6644257-83cf-4891-8e67-08c6640c9b6a
    url = "https://covid19-data.p.rapidapi.com/all"
    headers = {
        'x-rapidapi-host': "covid19-data.p.rapidapi.com",
        'x-rapidapi-key': "bd15e2cdccmshec0067fd8d4f01bp1cac7ejsnf9c59e492872"
    }

    res = requests.request("GET", url, headers=headers)
    res.raise_for_status()

    return res.json()


def generate_formatted_df(raw_data):
    df_formatted = DataFrame()

    country = []
    lat = []
    lon = []
    confirmed = []
    deaths = []
    recovered = []
    active = []

    for i in range(len(raw_data)):
        country.append(raw_data[i]["country"])
        lat.append(raw_data[i]["latitude"])
        lon.append(raw_data[i]["longitude"])
        confirmed.append(raw_data[i]["confirmed"])
        deaths.append(raw_data[i]["deaths"])
        recovered.append(raw_data[i]["recovered"])
        active.append(raw_data[i]["active"])

    df_formatted["country"] = country
    df_formatted["lon"] = lon
    df_formatted["lat"] = lat
    df_formatted["confirmed"] = confirmed
    df_formatted["deaths"] = deaths
    df_formatted["recovered"] = recovered
    df_formatted["active"] = active

    return df_formatted


def generate_confirmed_plot(df):
    map_confirmed = go.Scattermapbox(
        name='Confirmed Cases',
        lon=df['lon'],
        lat=df['lat'],
        text=df['country'],
        mode='markers',
        marker=go.scattermapbox.Marker(
            size=df['confirmed']/1000,
            color='orange',
            opacity=0.8
        )
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