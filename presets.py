import json
import glob

with open("presets.json", "w") as file:
    json.dump(glob.glob("presets/*"), file)
