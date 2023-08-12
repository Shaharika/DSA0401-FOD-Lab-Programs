import pandas as pd
data = {
    'property_id': [1, 2, 3, 4, 5],
    'location': ['City A', 'City B', 'City C', 'City D', 'City A '],
    'number_of_bedrooms': [2,4,6,7,8],
    'area_sqft': [1400, 1200, 1300, 1800, 1500],
    'listing_price': [250000, 26000, 300000, 400000, 350000]
}
data1= pd.DataFrame(data)
avg=data1.groupby('location')['listing_price'].mean()
bed1= data1[data1['number_of_bedrooms'] > 4]
bed2=len(bed1)
area=data1[data1['area_sqft']==data1['area_sqft'].max()]
print(avg)
print("Number of properties with more than four bedrooms:")
print(bed2)
print("Property with the largest area:")
print(area)



Output:
location
City A     250000.0
City A     350000.0
City B      26000.0
City C     300000.0
City D     400000.0
Name: listing_price, dtype: float64
Number of properties with more than four bedrooms:
3
Property with the largest area:
   property_id location  number_of_bedrooms  area_sqft  listing_price
3            4   City D                   7       1800         400000
