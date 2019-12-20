import pandas as pd
import numpy as np 
import sys
import os
from scipy.stats import iqr
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt


##from tensorflow import keras

df = pd.read_csv("US_Accidents_may19.csv")
df = df.drop(['ID', 'Source', 'TMC',
              'Start_Time', 'End_Time','Start_Lat', 
              'Start_Lng', 'End_Lat', 'End_Lng',
              'Description', 'Number', 'Street', 
              'Side', 'City', 'County', 'State',
              'Zipcode', 'Country', 'Timezone', 
              'Airport_Code', 'Weather_Timestamp',
              'Wind_Direction','Weather_Condition', 'Amenity', 'Bump',
              'Crossing','Give_Way', 'Junction', 
              'No_Exit', 'Railway', 'Roundabout', 
              'Station','Stop', 'Traffic_Calming', 
              'Traffic_Signal', 'Turning_Loop','Sunrise_Sunset',
              'Civil_Twilight', 'Nautical_Twilight','Astronomical_Twilight'],
                axis = 1)

df = df.rename(columns = {"Severity":'severity',
                    "Distance(mi)":'distance_affected',
                     "Temperature(F)":'temp',
                     "Wind_Chill(F)":'wind_chill',
                     'Humidity(%)':'humidity',
                     'Pressure(in)':'air_pressure',
                     'Visibility(mi)':'visibility', 
                     'Wind_Speed(mph)':'wind_speed',
                     'Precipitation(in)':'precipitation'})

df.describe()
df = df.interpolate()
df = df.dropna()
sum(np.where(df.isnull()))

plt.boxplot(df.distance_affected)
df.distance_affected.describe()
df.distance_affected = np.where(df.distance_affected >(1.5*.01 + .01),
                                (1.5*.01 +.01),df.distance_affected)


plt.boxplot(df.temp)
df.temp.describe()
df.temp = np.where(df.temp > (1.5*27 + 75.9),
                   (1.5*27 + 75.9),df.temp)
df.temp = np.where(df.temp <-10,-10,df.temp)

plt.boxplot(df.wind_chill)
plt.show()
df.wind_chill.describe()
df.wind_chill = np.where(df.wind_chill <-10,-10,df.wind_chill)

plt.boxplot(df.humidity)


plt.boxplot(df.air_pressure)
df.air_pressure.describe()
df.air_pressure = np.where(df.air_pressure > (1.5*iqr(df.air_pressure) + 30.15),
                           (1.5*iqr(df.air_pressure) + 30.15),df.air_pressure)
df.air_pressure = np.where(df.air_pressure < (29.92-1.5*iqr(df.air_pressure)),
                           (29.92-1.5*iqr(df.air_pressure)),df.air_pressure)

plt.boxplot(df.visibility)
df.visibility.describe()
df.visibility = np.where(df.visibility > 30,30,df.visibility)

plt.boxplot(df.wind_speed)
df.wind_speed = np.where(df.wind_speed > 80,80,df.wind_speed)

plt.boxplot(df.precipitation)
df.precipitation = np.where(df.precipitation >2,2,df.precipitation)


#####normalization
###normalized using (x-min)/(max-min)
distance = df.distance_affected
df.distance_affected = (distance - min(distance))/(max(distance)-min(distance))

temp = df.temp
df.temp = (temp - min(temp))/(max(temp)-min(temp))

windchill = df.wind_chill
df.wind_chill = (windchill - min(windchill))/(max(windchill)-min(windchill))

hum = df.humidity
df.humidity = (hum-min(hum))/(max(hum)-min(hum))

air = df.air_pressure
df.air_pressure = (air-min(air))/(max(air)-min(air))

vis = df.visibility
df.visibility = (vis-min(vis))/(max(vis)-min(vis))

wind = df.wind_speed
df.wind_speed = (wind-min(wind))/(max(wind)-min(wind))

prec = df.precipitation
df.precipitation = (prec-min(prec))/(max(prec)-min(prec))


train_data, test_data = train_test_split(df,test_size = .3)

train_data.to_csv("accidents_train.csv",index = False)
test_data.to_csv("accidents_test.csv",index = False)

df.describe()
df.corr()


