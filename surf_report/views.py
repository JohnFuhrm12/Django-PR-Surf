from django.shortcuts import render
import pandas as pd
import requests
import math

def home(request):
    # NDBC/NOAA API - San Juan Buoy (41053)
    BuoyInfo = pd.read_csv('https://www.ndbc.noaa.gov/data/realtime2/41053.txt', delim_whitespace=True)

    # OpenWeather API - San Juan Weather 
    WeatherInfo = requests.get('https://api.openweathermap.org/data/2.5/weather?lat=18.466986&lon=-66.089927&appid=73a95bf4ecd5b065a38ec246784e64ee').json()

    # Get Significant Wave Height - Converted to Meters and Feet
    WVHT_BC = BuoyInfo[pd.to_numeric(BuoyInfo.WVHT, errors='coerce').notnull()]
    WVHT_M = WVHT_BC.WVHT.iloc[0]
    WVHT_FT = round(float(WVHT_BC.WVHT.iloc[0]) * 3.28084, 2)

    # Get Dominant Wave Period
    DPD_BC = BuoyInfo[pd.to_numeric(BuoyInfo.DPD, errors='coerce').notnull()]
    PD = DPD_BC.DPD.iloc[0]

    # Get Water Temperature - Converted to Celsius and Fahrenheit
    WTEMP_BC = BuoyInfo[pd.to_numeric(BuoyInfo.WTMP, errors='coerce').notnull()]
    WTEMP_C = WTEMP_BC.WTMP.iloc[0]
    WTEMP_F = (float(WTEMP_C) * 1.80) + (float(32))

    # Get Wind Speed - Converted to Kilometers per hour and Miles per hour
    WSPD_BC = BuoyInfo[pd.to_numeric(BuoyInfo.WSPD, errors='coerce').notnull()]
    WSPD_KPH = round(float(WSPD_BC.WSPD.iloc[0]) * 3.60, 2)
    WSPD_MPH = round(float(WSPD_BC.WSPD.iloc[0]) * 2.2369, 2)

    # Get Wind Direction in all Cardinal Directions and Degrees
    WDIR_D = pd.DataFrame(WeatherInfo['wind'], index=['speed']).deg[0]
    DIR = 'N'

    if int(WDIR_D) == 0:
        DIR = 'N'
    if int(WDIR_D) > 0 and int(WDIR_D) < 45:
        DIR = 'NNE'
    if int(WDIR_D) == 45:
        DIR = 'NE'
    if int(WDIR_D) > 45 and int(WDIR_D) < 90:
        DIR = 'ENE'
    if int(WDIR_D) == 90:
        DIR = 'E'
    if int(WDIR_D) > 90 and int(WDIR_D) < 135:
        DIR = 'ESE'
    if int(WDIR_D) == 135:
        DIR = 'SE'
    if int(WDIR_D) > 135 and int(WDIR_D) < 180:
        DIR = 'SSE'
    if int(WDIR_D) == 180:
        DIR = 'S'
    if int(WDIR_D) > 180 and int(WDIR_D) < 225:
        DIR = 'SSW'
    if int(WDIR_D) == 225:
        DIR = 'SW'
    if int(WDIR_D) > 225 and int(WDIR_D) < 270:
        DIR = 'WSW'
    if int(WDIR_D) == 270:
        DIR = 'W'
    if int(WDIR_D) > 270 and int(WDIR_D) < 315:
        DIR = 'WNW'
    if int(WDIR_D) == 315:
        DIR = 'NW'
    if int(WDIR_D) > 315 and int(WDIR_D) < 0:
        DIR = 'NNW'
    
    # Get Current Weather Conditions
    Conditions = pd.DataFrame(WeatherInfo['weather']).description[0].title()

    # Get Air Temperature - Converted to Celsius and Fahrenheit
    Temperature = pd.DataFrame(WeatherInfo['main'], index=['temp'])
    Air_Temp_C = round(Temperature.temp[0] - 273.15)
    Air_Temp_F = round((Temperature.temp[0] - 273.15) * 1.8 + 32)

    # Get Wave Direction in all Cardinal Directions and Degrees
    MWD_BC = BuoyInfo[pd.to_numeric(BuoyInfo.MWD, errors='coerce').notnull()]
    WAVE_D = MWD_BC.MWD.iloc[0]
    WAVE_DIR = 'N'

    if int(WAVE_D) == 0:
        WAVE_DIR = 'N'
    if int(WAVE_D) > 0 and int(WAVE_D) < 45:
        WAVE_DIR = 'NNE'
    if int(WAVE_D) == 45:
        WAVE_DIR = 'NE'
    if int(WAVE_D) > 45 and int(WAVE_D) < 90:
        WAVE_DIR = 'ENE'
    if int(WAVE_D) == 90:
        WAVE_DIR = 'E'
    if int(WAVE_D) > 90 and int(WAVE_D) < 135:
        WAVE_DIR = 'ESE'
    if int(WAVE_D) == 135:
        WAVE_DIR = 'SE'
    if int(WAVE_D) > 135 and int(WAVE_D) < 180:
        WAVE_DIR = 'SSE'
    if int(WAVE_D) == 180:
        WAVE_DIR = 'S'
    if int(WAVE_D) > 180 and int(WAVE_D) < 225:
        WAVE_DIR = 'SSW'
    if int(WAVE_D) == 225:
        WAVE_DIR = 'SW'
    if int(WAVE_D) > 225 and int(WAVE_D) < 270:
        WAVE_DIR = 'WSW'
    if int(WAVE_D) == 270:
        WAVE_DIR = 'W'
    if int(WAVE_D) > 270 and int(WAVE_D) < 315:
        WAVE_DIR = 'WNW'
    if int(WAVE_D) == 315:
        WAVE_DIR = 'NW'
    if int(WAVE_D) > 315 and int(WAVE_D) < 0:
        WAVE_DIR = 'NNW'

    # Get wave height ranges 
    WVHT_MIN_F = math.floor(float(WVHT_FT))
    WVHT_MAX_F = math.ceil(float(WVHT_FT))
    WVHT_MIN_M = math.floor(float(WVHT_M))
    WVHT_MAX_M = math.ceil(float(WVHT_M))

    # Wave quality
    WAVE_QUALITY = 'Fair'
    if float(WVHT_FT) < 1:
        WAVE_QUALITY = 'Flat'
    # If 15mph+ winds and onshore - than
    if float(WSPD_MPH) > 15 and (float(WDIR_D) > 45 or float(WDIR_D) < 225):
        WAVE_QUALITY = 'Poor'
    # If less than 20mph winds and waveheight over 2ft and offshore - than
    if float(WSPD_MPH) < 20 and float(WVHT_FT) > 2 and (float(WDIR_D) < 45 or float(WDIR_D) > 225):
        WAVE_QUALITY = 'Fair'
    # If less than 5mph winds and waveheight over 2ft and onshore - than
    if float(WSPD_MPH) < 5 and float(WVHT_FT) > 2 and (float(WDIR_D) > 45 or float(WDIR_D) < 225):
        WAVE_QUALITY = 'Fair'
    # If less than 10mph winds and waveheight over 4ft and offshore - than
    if float(WVHT_FT) > 4 and float(WSPD_MPH) < 10 and (float(WDIR_D) < 45 or float(WDIR_D) > 225):
        WAVE_QUALITY = 'Great'
    # If less than 10mph winds and waveheight over 6ft and offshore - than
    if float(WVHT_FT) > 6 and float(WSPD_MPH) < 10 and (float(WDIR_D) < 45 or float(WDIR_D) > 225):
        WAVE_QUALITY = 'Firing'

    # Usable Variables in HTML File
    content = {
        'wvht_m': WVHT_M,
        'wvht_ft': WVHT_FT,
        'pd': PD,
        'wtemp_c': WTEMP_C,
        'wtemp_f': WTEMP_F,
        'wspd_kph': WSPD_KPH,
        'wspd_mph': WSPD_MPH,
        'wdir_d': WDIR_D,
        'dir': DIR,
        'conditions': Conditions,
        'air_temp_c': Air_Temp_C,
        'air_temp_f': Air_Temp_F,
        'wave_d': WAVE_D,
        'wave_dir': WAVE_DIR,
        'wvht_min_f': WVHT_MIN_F,
        'wvht_max_f': WVHT_MAX_F,
        'wvht_min_m': WVHT_MIN_M,
        'wvht_max_m': WVHT_MAX_M,
        'wave_quality': WAVE_QUALITY,
    }

    return render(request, 'index.html', content)