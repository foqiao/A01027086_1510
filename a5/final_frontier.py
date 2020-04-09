import time
import datetime
import requests
import json

def final_frontier(url: str):
    response = requests.get(url)
    with open(response.text, "r") as frontier:
        for frontier_Read in frontier:
            frontier_read = frontier.readline(1)
            print(frontier)
            time.sleep(300)

def main():
    url = "https://exoplanetarchive.ipac.caltech.edu/cgi-bin/nstedAPI/nph-nstedAPI?&table=exoplanets&format=ipac&where=pl_kepflag=1"
    final_frontier(url)
    func = final_frontier(url)
    recorder(func)

if __name__ == '__main__':
    main()