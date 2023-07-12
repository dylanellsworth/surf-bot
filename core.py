import surf_spots
import datetime

# DEFINE GLOBAL VARIABLES
spots_path = "spots.json"
spots_db = surf_spots.init_surf_spot_db(spots_path)

def timestamp_to_datetime(timestamp):
    '''
    Returns datetime object given a timestamp.

    Parameters:
      timestamp(int): Name of the surf spot

    Returns:
      datetime object
    '''    
    dt_obj = datetime.datetime.fromtimestamp(timestamp)
    return dt_obj

def degrees_to_cardinal(deg):
    '''
    Returns cardinal direction given a direction in degrees.

    Parameters:
      deg(int): direction in degrees

    Returns:
      card_dir(str): cardinal direction
    '''
    card_dir = ""
    if ((deg >= 348.75 and deg <= 360) or (deg <= 11.25 and deg >= 0)):
        card_dir = "N"
    elif (deg >= 11.25 and deg <= 33.75):
        card_dir = "NNE"
    elif (deg >= 33.75 and deg <= 56.25):
        card_dir = "NE"
    elif (deg >= 56.25 and deg <= 78.75):
        card_dir = "ENE"
    elif (deg >= 78.75 and deg <= 101.25):
        card_dir = "E"
    elif (deg >= 101.25 and deg <= 123.75):
        card_dir = "ESE"
    elif (deg >= 123.75 and deg <= 146.25):
        card_dir = "SE"
    elif (deg >= 146.25 and deg <= 168.75):
        card_dir = "SSE"
    elif (deg >= 168.75 and deg <= 191.25):
        card_dir = "S"
    elif (deg >= 191.25 and deg <= 213.75):
        card_dir = "SSW"
    elif (deg >= 213.75 and deg <= 236.25):
        card_dir = "SW"
    elif (deg >= 236.25 and deg <= 258.75):
        card_dir = "WSW"
    elif (deg >= 258.75 and deg <= 281.25):
        card_dir = "W"
    elif (deg >= 281.25 and deg <= 303.75):
        card_dir = "WNW"
    elif (deg >= 303.75 and deg <= 326.25):
        card_dir = "NW"
    elif (deg >= 326.25 and deg <= 348.75):
        card_dir = "NNW"
    else :
        raise ValueError("Cannot convert degrees to cardinal. Invalid input: '", deg, "'")
    return card_dir