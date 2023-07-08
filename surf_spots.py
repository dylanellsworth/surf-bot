import json

class SurfSpot:
    def __init__(self, name, id, url):
        self.name = name
        self.id = id
        self.url = url

# Load the surf spot db from the json file
def init_surf_spot_db():
    spot_dict = {}
    spots_file = open("spots.json")
    spots_json = json.load(spots_file)
    for spot in spots_json["spots"]:
        spot_dict.update({spot["name"]: SurfSpot(spot["name"], spot["id"], spot["url"])})
    return spot_dict

# Initialize the spot database
spot_db = init_surf_spot_db()

# look up the spot id given a spot name
def get_spot_id(spot_name):
    spot_id = spot_db.get(spot_name).id
    if (spot_id):
        return spot_id
    else:
        raise KeyError("Surf spot does not exist: '" + spot_name + "'" )

# look up the spot name given a spot id
def get_spot_name(spot_id):
    # Iterate through spot dictionary to find matching id
    for key, value in spot_db.items():
        if spot_id == value.id:
            return key
    # spot id does not appear in the dictionary
    raise KeyError("Surf spot id does not exist: '" + spot_id + "'" )