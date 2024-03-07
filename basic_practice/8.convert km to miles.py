#coverting km to miles
distance = float(input('enter distance: '))
units=input('units of a distance are km or mils: ')
if units.lower() == "km":
    conv_miles = 0.62137*distance
    print(f'the converted value in miles is {conv_miles}')
else:
    conv_km = distance/0.62137
    print(f'the converted value in miles is {conv_km}')

