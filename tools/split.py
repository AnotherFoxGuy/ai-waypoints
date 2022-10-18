import json
import os

waypoints = open("waypoints.json", "r")
data = json.loads(waypoints.read())


for d in data:
    name = d["terrain"].replace(".terrn2", "")
    name += "_" + d["preset"].replace(" ", "_") + ".json"
    f = open(os.path.join(os.getcwd(), "waypoints", name.lower()), "w")
    f.write(json.dumps(d, indent=4))
    f.close()
