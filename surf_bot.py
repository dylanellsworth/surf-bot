import surf_report
import core

# Get forecast
spot_name = "Blacks"
forecast = surf_report.get_spot_forecast(spot_name, 5, 1)

# Sort wave forecast
wave_sort_key = "surf_humanRelation"
forecast.wave.sort(key = lambda x: x[wave_sort_key], reverse=True)

# Print sorted wave forecast
for wave in forecast.wave:
    wave_time = core.timestamp_to_datetime(wave["timestamp"])
    wave_size = wave["surf_humanRelation"]
    wave_min = wave["surf_min"]
    wave_max = wave["surf_max"]
    wave_power = wave["power"]
    print(wave_time, " ", wave_size , "  ", wave_min,"-",wave_max, "ft   ", wave_power)

# Sort wind foreceast
forecast.wind.sort(key = lambda x: x["directionType"], reverse=False)
for wind in forecast.wind:
    wind_time = core.timestamp_to_datetime(wind["timestamp"])
    wind_speed = wind["speed"]
    wind_dir = wind["direction"]
    wind_dir_type = wind["directionType"]
    print(wind_time, " ", wind_speed , "  ", wind_speed, "mph", wind_dir, wind_dir_type)
