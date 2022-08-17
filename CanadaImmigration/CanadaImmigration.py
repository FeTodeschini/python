import pandas as pd
import matplotlib as mtp
import matplotlib.pyplot as plt

countryRequired = True

while countryRequired:
    try:
        country = input("Type the name of the country for which you want to see the number of immigrants to Canada from 1980 to 2013: ").capitalize()

        df = pd.read_csv("canadian_immegration_data.csv")
        years = list(map(str, range(1980,2013)))

        df.set_index('Country', inplace=True)

        #filters the dataframe
        df.loc[country, years].plot(kind = 'line')


        #configures the chart
        plt.title("Immigration to Canada from " + country)
        plt.ylabel("Number of Immigrants")
        plt.xlabel("years")

        # #display the chart
        plt.show()
        countryRequired = False
    
    except KeyError:
        print(country + " is not a country in the list")

