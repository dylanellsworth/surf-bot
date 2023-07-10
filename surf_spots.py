import json

class SurfSpot:
    def __init__(self, name, id, url):
        self.name = name
        self.id = id
        self.url = url

class SurfSpotDB:
    def __init__(self, spots):
        self.spots = spots

    def get_spot_id(self, spot_name):
        '''
        Get the spot id for the provided spot if it exists

        Parameters:
          spot_name(str): Name of the spot

        Returns:
          spot_id(int)
        '''
        spot_id = self.spots.get(spot_name).id
        if (spot_id):
            return spot_id
        else:
            raise KeyError("Surf spot does not exist: '" + spot_name + "'" )
        
    # look up the spot name given a spot id
    def get_spot_name(self, spot_id):
        # Iterate through spot dictionary to find matching id
        for key, value in self.spots.items():
            if spot_id == value.id:
                return key
        # spot id does not appear in the dictionary
        raise KeyError("Surf spot id does not exist: '" + spot_id + "'" )

def init_surf_spot_db(spots_path):
    '''
    Create surf spot database from the provided json file.

    Parameters:
      spots_path(str): Path to the spots json file

    Returns:
      SurfSpotDB object
    '''
    spot_dict = {}
    spots_file = open(spots_path)
    spots_json = json.load(spots_file)
    for spot in spots_json["spots"]:
        spot_dict.update({spot["name"]: SurfSpot(spot["name"], spot["id"], spot["url"])})
    return SurfSpotDB(spot_dict)