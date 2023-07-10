from pysurfline import SurfReport, SpotForecast
import core

def get_spot_report(spot_name, days, hour_interval):
    '''
    Returns the surf report for a given spot.

    Parameters:
      spot_name(str): Name of the surf spot
      days(int): number of days to include in the report
      hour_interval(int): interval of hours in the report

    Returns:
      SurfReport object
    '''
    try:
        spot_id = core.spots_db.get_spot_id(spot_name)
        params = {
            "spotId": spot_id,
            "days": days,
            "intervalHours": hour_interval
            }
        report = SurfReport(params)
        return report
    except KeyError as err:
        print(err)


def get_spot_forecast(spot_name, days, hour_interval):
    '''
    Returns the forecast for a given spot.

    Parameters:
      spot_name(str): Name of the surf spot
      days(int): number of days to include in the forecast
      hour_interval(int): interval of hours in the forecast

    Returns:
      SurfForecast object
    '''
    try:
        spot_id = core.spots_db.get_spot_id(spot_name)
        params = {
            "spotId": spot_id,
            "days": days,
            "intervalHours": hour_interval
            }
        report = SpotForecast(params)
        return report
    except KeyError as err:
        print(err)