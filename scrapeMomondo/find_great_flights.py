
import pandas as pd


results = pd.read_csv('results.csv')
results = results[results.DepartureTime > '18:00']

airportcodes = pd.read_csv('airports_codes.txt',sep='\t')

for iid in results.id.unique():
    tmp = results[results['id']==iid].sort_values('Rating',ascending=False)
    cph = tmp[tmp['DepartureAirport']=='CPH'].reset_index(drop=True)[:1]
    not_cph = tmp[tmp['DepartureAirport']!='CPH'].reset_index(drop=True)[:1]

    dest = airportcodes.loc[airportcodes.AirportCode==cph.loc[0,'ArrivalAirport'],'CityName'].values[0]

    for _ in range(3):
        print()

    print("""Trip to {} on the {} at {}, at price of {}.
Returning to CPH on {} at {} at a price of {}. Total price of {}.
Ratings {} and {}.\nTravel times {} and {}""".format(dest.title().strip(),cph.loc[0,'Date'],
                                                         cph.loc[0,'DepartureTime'],cph.loc[0,'Price'],
                                                         not_cph.loc[0,'Date'],not_cph.loc[0,'DepartureTime'],
                                                         not_cph.loc[0,'Price'],cph.loc[0,'Price'] + not_cph.loc[0,'Price'],
                                                         cph.loc[0,'Rating'],not_cph.loc[0,'Rating'],
                                                         cph.loc[0,'Duration'],not_cph.loc[0,'Duration']))



