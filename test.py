temp = ['neighbourhood_group_cleansed_Mitte', 'neighbourhood_group_cleansed_Friedrichshain-Kreuzberg', 'neighbourhood_group_cleansed_Pankow', 'neighbourhood_group_cleansed_Tempelhof - Schöneberg', 'neighbourhood_group_cleansed_Steglitz - Zehlendorf', 'neighbourhood_group_cleansed_Neukölln', 'neighbourhood_group_cleansed_Spandau', 'neighbourhood_group_cleansed_Charlottenburg-Wilm.', 'neighbourhood_group_cleansed_Lichtenberg', 'neighbourhood_group_cleansed_Reinickendorf', 'neighbourhood_group_cleansed_Treptow - Köpenick', 'neighbourhood_group_cleansed_Marzahn - Hellersdorf', 'room_type_Private room', 'room_type_Entire home/apt', 'room_type_Shared room', 'accommodates', 'bathrooms', 'bedrooms', 'beds', 'bed_type_Real Bed', 'bed_type_Couch', 'bed_type_Futon', 'bed_type_Pull-out Sofa', 'bed_type_Airbed', 'security_deposit', 'cleaning_fee', 'minimum_nights', 'Washer', 'Hair dryer', 'Laptop friendly workspace', 'Hangers', 'Iron', 'Shampoo', 'TV', 'Hot water', 'Family/kid friendly', 'Internet', 'Host greets you', 'Smoke detector', 'Buzzer/wireless intercom', 'Lock on bedroom door', 'Free street parking', 'Elevator', 'Bed linens', 'Smoking allowed', 'First aid kit', 'Cable TV'] 
temp2 = ['accommodates', 'bedrooms', 'bathrooms', 'beds', 'security_deposit', 'cleaning_fee', 'minimum_nights', 'bed_type_Real Bed', 'bed_type_Couch', 'bed_type_Futon', 'bed_type_Pull-out Sofa', 'bed_type_Airbed', 'room_type_Private room', 'room_type_Entire home/apt', 'room_type_Shared room', 'neighbourhood_group_cleansed_Mitte', 'neighbourhood_group_cleansed_Friedrichshain-Kreuzberg', 'neighbourhood_group_cleansed_Pankow', 'neighbourhood_group_cleansed_Tempelhof - Schöneberg', 'neighbourhood_group_cleansed_Steglitz - Zehlendorf', 'neighbourhood_group_cleansed_Neukölln', 'neighbourhood_group_cleansed_Spandau', 'neighbourhood_group_cleansed_Charlottenburg-Wilm.', 'neighbourhood_group_cleansed_Lichtenberg', 'neighbourhood_group_cleansed_Reinickendorf', 'neighbourhood_group_cleansed_Treptow - Köpenick', 'neighbourhood_group_cleansed_Marzahn - Hellersdorf', 'Washer', 'Hair dryer', 'Laptop friendly workspace', 'Hangers', 'Iron', 'Shampoo', 'TV', 'Hot water', 'Family/kid friendly', 'Internet', 'Host greets you', 'Smoke detector', 'Buzzer/wireless intercom', 'Lock on bedroom door', 'Free street parking', 'Elevator', 'Bed linens', 'Smoking allowed', 'First aid kit', 'Cable TV']

res = []
res2 = []

for var in temp:
    if var not in temp2:
        res.append(var)

for var in temp2:
    if var not in temp:
        res2.append(var)

for tup in zip(res, res2):
    print(tup)