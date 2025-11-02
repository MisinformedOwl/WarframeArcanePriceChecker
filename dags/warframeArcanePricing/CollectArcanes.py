import requests
from time import sleep
import json
from pathlib import Path
import pandas as pd

def grabSalesStats(arcaneName: str) -> int:
    """
    Based off the API call https://api.warframe.market/v1/items/arcane_hot_shot/statistics
    This is used to collect the average sell amount within the last 48 hours per hour for use in valuation.

    ## Parameters
    - _arcaneName_: The name of the arcane to get the statistics of. lower case

    ## Returns
    - Int
    """
    sleep(0.5)
    baseURL = "https://api.warframe.market/v1/"
    data = requests.get(baseURL+f"items/{arcaneName}/statistics").json()
    saleVolumes = []

    data = data["payload"]["statistics_closed"]["48hours"]
    data = [entry for entry in data if entry["mod_rank"] == 5 or entry["mod_rank"] == 3]

    for arcane in data:
        saleVolumes.append(arcane["volume"])
    try:
        return sum(saleVolumes)/48 # 48 hours
    except ZeroDivisionError as ex:
        return 1

def scrapePrice(arcaneName: str) -> int:
    """
    This function is designed to interact with the API of warframe marketplace.
    It navigates to an example url: https://api.warframe.market/v2/orders/item/arcane_hot_shot/top?&rank=5 This is for arcane hotshot.

    It collects only the top orders, of those selling at rank 5. The top orders end up being only 5.

    ## Parameters
    - _arcaneName_: The name of the arcane to get the price for. lower case

    ## Returns
    - Int
    """
    baseURL = "https://api.warframe.market/v2/"
    data = requests.get(baseURL+f"orders/item/{arcaneName}/top?&rank=5").json()
    prices = []

    try:
        orders = data["data"]["sell"]
    except TypeError as ex:
        data = requests.get(baseURL+f"orders/item/{arcaneName}/top?&rank=3").json()
        orders = data["data"]["sell"]
    
    for d in orders:
        prices.append(d["platinum"])
    
    if len(prices) == 0:
        return 0
    price = sum(prices)/len(prices)
    return price

def priceArcanes():
    """
    This function rolls through arcanes and grabs the current prices for each on warframe marketplace.
    And then calculates the value proposition based on the chance to get it compared to it's current market price.
    It then stores the data in a csv which can be accessed by power BI.
    """
    with open(Path(__file__).parent / "ArcaneList.json") as f:
        data = json.load(f)

    rows = []

    for arcane in data[0]["Arcanes"]:
        try:
            sleep(0.5)
            name = arcane["Name"]
            price = scrapePrice(name.lower())
            volume = grabSalesStats(name.lower())

            print(f"{name}: {price}")

            chance = arcane["DropChance"]
            valueProp = (price/100)*chance
            arcane["ValueProposition"] = valueProp

            rows.append({
                "Name" : name,
                "DropChance": chance,
                "Price": price,
                "ValueProposition": valueProp,
                "Volume": volume,
                "Faction": arcane["Faction"]
            })
            
        except TypeError as ex:
            print(f"{name} was inaccessible.")
            rows.append({
                "Name" : name,
                "DropChance": chance,
                "Price": 0,
                "ValueProposition": 0,
                "Faction": arcane["Faction"]
            })
    
    frame = pd.DataFrame(rows)
    frame.to_csv(Path(__file__).parent / "ArcanePriceAnalysis.csv")
