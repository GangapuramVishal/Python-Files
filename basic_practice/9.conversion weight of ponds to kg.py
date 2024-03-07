weight = int(input("enter your weight =  "))
units = input('lbs or kg : ' ) 
if units.lower() == "lbs" :
    converted_weight_kg = weight * 0.45
    print(f'the converted weight in kg is {converted_weight_kg} kg')
else :
    converted_weight_lbs = weight / 0.45
    print(f'the converted weight in lbs is {converted_weight_lbs} lbs')
