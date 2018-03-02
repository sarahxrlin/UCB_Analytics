
Observable trends:

1) Cloudiness does not change across latitudes

2) Temperature increases as you move closer to the equator

3) Wind speed increases as you move away from the equator


```python
#import dependencies
import requests
from pprint import pprint
import json
import citipy
import openweathermapy.core as owm
import random
import pandas as pd
```


```python
# import api_key
from weather_api import api_key
```


```python
# grab 500 random cities in worldcities.csv
city_data = pd.read_csv('citipy-0.0.5/citipy/worldcities.csv')
city_data.head()
len(city_data)
```




    46832




```python
city_sample = city_data.sample(10) #I can change this number to 500, but did 20 to save space
city_sample.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Country</th>
      <th>City</th>
      <th>Latitude</th>
      <th>Longitude</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>45939</th>
      <td>us</td>
      <td>montclair</td>
      <td>38.610833</td>
      <td>-77.340000</td>
    </tr>
    <tr>
      <th>26220</th>
      <td>nz</td>
      <td>kaitangata</td>
      <td>-46.275000</td>
      <td>169.850000</td>
    </tr>
    <tr>
      <th>35947</th>
      <td>ru</td>
      <td>gremyachye</td>
      <td>51.974200</td>
      <td>38.800100</td>
    </tr>
    <tr>
      <th>5509</th>
      <td>ch</td>
      <td>therwil</td>
      <td>47.501166</td>
      <td>7.552859</td>
    </tr>
    <tr>
      <th>11304</th>
      <td>fi</td>
      <td>valkeakoski</td>
      <td>61.266667</td>
      <td>24.033333</td>
    </tr>
  </tbody>
</table>
</div>




```python
#iterate through the list of cities and perform a request for data on each
weather_json = []

city_count = 1

# set up params
params = {"appid": api_key,
          "units": "imperial"}

for index, row in city_sample.iterrows():

    # update params with zipcode each loop
    params['q'] = row['City']

    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    # Print log to ensure loop is working correctly
    print("Now retrieving city # " + str(city_count) + ": " + row['City'])
    city_count += 1

    # Run requests to grab the JSON at the requested URL
    response = requests.get(base_url, params=params)
    print(response.url)

    response_json = response.json()
    weather_json.append(response_json)
```

    Now retrieving city # 1: montclair
    http://api.openweathermap.org/data/2.5/weather?appid=efbe68058e19e818378ea254e7ccdb09&units=imperial&q=montclair
    Now retrieving city # 2: kaitangata
    http://api.openweathermap.org/data/2.5/weather?appid=efbe68058e19e818378ea254e7ccdb09&units=imperial&q=kaitangata
    Now retrieving city # 3: gremyachye
    http://api.openweathermap.org/data/2.5/weather?appid=efbe68058e19e818378ea254e7ccdb09&units=imperial&q=gremyachye
    Now retrieving city # 4: therwil
    http://api.openweathermap.org/data/2.5/weather?appid=efbe68058e19e818378ea254e7ccdb09&units=imperial&q=therwil
    Now retrieving city # 5: valkeakoski
    http://api.openweathermap.org/data/2.5/weather?appid=efbe68058e19e818378ea254e7ccdb09&units=imperial&q=valkeakoski
    Now retrieving city # 6: woudrichem
    http://api.openweathermap.org/data/2.5/weather?appid=efbe68058e19e818378ea254e7ccdb09&units=imperial&q=woudrichem
    Now retrieving city # 7: cajetina
    http://api.openweathermap.org/data/2.5/weather?appid=efbe68058e19e818378ea254e7ccdb09&units=imperial&q=cajetina
    Now retrieving city # 8: gola gokarannath
    http://api.openweathermap.org/data/2.5/weather?appid=efbe68058e19e818378ea254e7ccdb09&units=imperial&q=gola+gokarannath
    Now retrieving city # 9: ondangwa
    http://api.openweathermap.org/data/2.5/weather?appid=efbe68058e19e818378ea254e7ccdb09&units=imperial&q=ondangwa
    Now retrieving city # 10: west palm beach
    http://api.openweathermap.org/data/2.5/weather?appid=efbe68058e19e818378ea254e7ccdb09&units=imperial&q=west+palm+beach



```python
# Latitude
lat_data = [data.get("coord").get("lat") for data in weather_json]

# Temperature F
temp_data = [data.get("main").get("temp") for data in weather_json]

# Humidity (%)
humidity_data = [data.get("main").get("humidity") for data in weather_json]

# Cloudiness (%)
cloud_data = [data.get("clouds").get("all") for data in weather_json]

# Wind Speed (mph)
wind_data = [data.get("wind").get("speed") for data in weather_json]

# city name
city = [data.get("name") for data in weather_json]

```


    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    <ipython-input-195-78dc82a824cb> in <module>()
          1 # Latitude
    ----> 2 lat_data = [data.get("coord").get("lat") for data in weather_json]
          3 
          4 # Temperature F
          5 temp_data = [data.get("main").get("temp") for data in weather_json]


    <ipython-input-195-78dc82a824cb> in <listcomp>(.0)
          1 # Latitude
    ----> 2 lat_data = [data.get("coord").get("lat") for data in weather_json]
          3 
          4 # Temperature F
          5 temp_data = [data.get("main").get("temp") for data in weather_json]


    AttributeError: 'NoneType' object has no attribute 'get'



```python
weather_dict = {"City":city, "Latitude": lat_data, "Temperature (Fahrenheit)": temp_data, 
                "Humidity (%)": humidity_data, "Cloudiness (%)": cloud_data, 
                "Wind Speed (mph)": wind_data
               }
weather_df = pd.DataFrame(weather_dict)

weather_df.to_csv("weather_final.csv")

weather_df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>City</th>
      <th>Cloudiness (%)</th>
      <th>Humidity (%)</th>
      <th>Latitude</th>
      <th>Temperature (Fahrenheit)</th>
      <th>Wind Speed (mph)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Pyatigorsk</td>
      <td>90</td>
      <td>100</td>
      <td>44.04</td>
      <td>30.20</td>
      <td>6.71</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Bunawan</td>
      <td>40</td>
      <td>74</td>
      <td>7.24</td>
      <td>80.60</td>
      <td>4.70</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Yanji</td>
      <td>0</td>
      <td>57</td>
      <td>42.89</td>
      <td>12.77</td>
      <td>8.66</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Ligatne</td>
      <td>76</td>
      <td>80</td>
      <td>57.23</td>
      <td>12.32</td>
      <td>8.99</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Tiko</td>
      <td>40</td>
      <td>100</td>
      <td>4.08</td>
      <td>75.20</td>
      <td>3.40</td>
    </tr>
  </tbody>
</table>
</div>




```python
weather_df.set_index("City", inplace=True)
weather_df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Cloudiness (%)</th>
      <th>Humidity (%)</th>
      <th>Latitude</th>
      <th>Temperature (Fahrenheit)</th>
      <th>Wind Speed (mph)</th>
    </tr>
    <tr>
      <th>City</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Pyatigorsk</th>
      <td>90</td>
      <td>100</td>
      <td>44.04</td>
      <td>30.20</td>
      <td>6.71</td>
    </tr>
    <tr>
      <th>Bunawan</th>
      <td>40</td>
      <td>74</td>
      <td>7.24</td>
      <td>80.60</td>
      <td>4.70</td>
    </tr>
    <tr>
      <th>Yanji</th>
      <td>0</td>
      <td>57</td>
      <td>42.89</td>
      <td>12.77</td>
      <td>8.66</td>
    </tr>
    <tr>
      <th>Ligatne</th>
      <td>76</td>
      <td>80</td>
      <td>57.23</td>
      <td>12.32</td>
      <td>8.99</td>
    </tr>
    <tr>
      <th>Tiko</th>
      <td>40</td>
      <td>100</td>
      <td>4.08</td>
      <td>75.20</td>
      <td>3.40</td>
    </tr>
    <tr>
      <th>Clara</th>
      <td>92</td>
      <td>88</td>
      <td>53.34</td>
      <td>32.34</td>
      <td>30.91</td>
    </tr>
    <tr>
      <th>Chigasaki</th>
      <td>1</td>
      <td>29</td>
      <td>35.33</td>
      <td>49.24</td>
      <td>6.93</td>
    </tr>
    <tr>
      <th>Assen</th>
      <td>20</td>
      <td>62</td>
      <td>53.00</td>
      <td>21.20</td>
      <td>21.92</td>
    </tr>
    <tr>
      <th>Sitamau</th>
      <td>0</td>
      <td>76</td>
      <td>24.01</td>
      <td>61.95</td>
      <td>3.40</td>
    </tr>
    <tr>
      <th>Velur</th>
      <td>20</td>
      <td>83</td>
      <td>10.64</td>
      <td>78.03</td>
      <td>5.82</td>
    </tr>
  </tbody>
</table>
</div>




```python
temp_plot = weather_df.plot(kind="scatter",
                x="Latitude", 
                y="Temperature (Fahrenheit)",
                marker="o",
                title="Temperature in World Cities",
                grid=True
               );

fig = temp_plot.get_figure()
fig.savefig("TemperatureWorldCities.png");
```


![png](output_9_0.png)



```python
humidity_plot = weather_df.plot(kind="scatter",
                x="Latitude", 
                y="Humidity (%)",
                marker="o",
                title="Humidity in World Cities",
                grid=True
               );

fig = humidity_plot.get_figure()
fig.savefig("HumidityWorldCities.png");
```


![png](output_10_0.png)



```python
cloud_plot = weather_df.plot(kind="scatter",
                x="Latitude", 
                y="Cloudiness (%)",
                marker="o",
                title="Cloudiness in World Cities",
                grid=True
               );

fig = cloud_plot.get_figure()
fig.savefig("CloudinessWorldCities.png");
```


![png](output_11_0.png)



```python
wind_plot = weather_df.plot(kind="scatter",
                x="Latitude", 
                y="Wind Speed (mph)",
                marker="o",
                title="Wind Speed in World Cities",
                grid=True
               );

fig = wind_plot.get_figure()
fig.savefig("WindWorldCities.png");
```


![png](output_12_0.png)

