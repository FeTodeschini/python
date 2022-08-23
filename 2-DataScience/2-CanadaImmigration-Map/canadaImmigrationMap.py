from unicodedata import name
import pandas as pd
import folium

import matplotlib as mtp
import matplotlib.pyplot as plt

df = pd.read_csv("canadian_immegration_data.csv")

worldMap = folium.Map(
    zoom_start = 2
)

worldGeoFile = r'canadaimmigrationmap.json'

worldMap.Choropleth(
    geo_data=worldGeoFile
    , data=df
    , column = ['Country', 'Total']
    , key_on = 'feature.properties.name'
    , fill_color='YlOrRd'
    , legend_name='Immigration to Canada'
)

worldMap

# df.set_index('Country', inplace=True)

# #filters the dataframe
# df.loc[country, years].plot(kind = 'line')


# #configures the chart
# plt.title("Immigration to Canada from " + country)
# plt.ylabel("Number of Immigrants")
# plt.xlabel("years")

# # #display the chart
# plt.show()
