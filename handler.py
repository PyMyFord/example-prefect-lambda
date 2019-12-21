import os
from prefect import FordAPI
import json


def handler(params):

    F = FordAPI()
    F.authenticate(os.environ.get("prefectuser"), os.environ.get("prefectpass"))
    F.get_vehicles() # returns a list of dicts with metadata
    my_car = F.get_vehicles()[0]

    my_car.start_engine()

    return json.dumps(my_car.status()) # metadata dictionary
