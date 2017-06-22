"""Our team wants to offer customers the ability to request on-demand
showings where a showing agent drives to a chosen property at a certain
time and shows the property to potential buyers. To create the system that
routes requests to agents whoa re nearby we need to know the driving distance
from a given showing agent's location to the given property. The team is
considering using the Google Distance Matrix API. Create a wrapper that makes
the API easy to use, as a minimal implementation have it take as arguments

- a single origin, an address formatted as a string, e.g. "2301 Hyperion Ave,
Los Angeles, CA 90027
- a single destination formatted in the same way
- a time of departure formatted as a standard date or time object

and have the wrapper return a number that represents the driving
distance in miles. Additionally, if you were going to continue implementing
a more feature rich version of this wrapper what other features would be useful?"""


# other features:
# fuzzy predictive searching or more lenient auto parsing of inputs
# travel time estimation for the agent based on time of day (available)
# simple interface for user to select departure time

import datetime as dt
import requests

def showing_distance():
    print("What is your current location, please use the following format as a template")
    print("2301 Hyperion Ave Los Angeles CA 90027")
    # connect starting destination with + for query string
    location = input().strip().replace(' ', '+')

    print("What is your destination, please use the following format as a template")
    print("9237 Regents Road La Jolla CA 92037")
    destination = input().strip().replace(' ', '+')

    print("What time will you be leaving, please use the following time format")
    print("HH:MM in 24 hour time")
    leaving_time = list(map(lambda x: int(x), input().strip().split(":")))
    hour, minute = leaving_time[0], leaving_time[1]

    print("What day will you be leaving, please use the following date format")
    print("DD/MM/YYYY")
    leaving_date = list(map(lambda x: int(x), input().strip().split("/")))
    day, month, year = leaving_date[0], leaving_date[1], leaving_date[2]
    leaving = dt.datetime(year=year, month=month, day=day, hour=hour, minute=minute)
    unix_time = dt.datetime(1970, 1, 1)
    seconds = int((leaving - unix_time).total_seconds())

    r = requests.get(f"https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&origins={location}&destinations={destination}&departure_time={seconds}&key=INSERT_API_KEY_HERE")
    print("")
    distance = r.json()['rows'][0]['elements'][0]['distance']['text']
    print(f"You will have to drive {distance}")

showing_distance()
