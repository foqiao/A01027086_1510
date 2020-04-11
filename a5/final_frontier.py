import time
import datetime
import requests
import json

def final_frontier(url: str):
    response = requests.get(url)
    response.raise_for_status()
    frontier = json.loads(response.text)
    print(f"planet hostname: {frontier[0]['pl_hostname']}")
    print(f"planet letter: {frontier[0]['pl_letter']}")
    print(f"planet name: {frontier[0]['pl_name']}")
    print(f"planet disc method: {frontier[0]['pl_discmethod']}")
    time.sleep(300)

def main():
    url = "https://exoplanetarchive.ipac.caltech.edu/cgi-bin/nstedAPI/nph-nstedAPI?table=exoplanets&format=json"
    final_frontier(url)

if __name__ == '__main__':
    main()