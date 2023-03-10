import phonenumbers
import opencage
import folium
from myphone import number

from phonenumbers import geocoder
from phonenumbers import carrier
from opencage.geocoder import OpenCageGeocode

my_number = phonenumbers.parse(number, region='FI')
Carrier = carrier.name_for_number(my_number, 'en')
Region = geocoder.description_for_number(my_number, "en")
my_location = geocoder.description_for_number(my_number, "en", region='FI')

key = 'acf2df2dfffb4cb484ae7a25c8ea444c'
geocoder = OpenCageGeocode(key)
query = str(my_location)
results = geocoder.geocode(query)

lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']

print(lat,lng)
#print(my_number)
print(my_location)
print(Carrier)
print(results)

myMap = folium.Map(location=[lat, lng], zoom_start=10)
folium.Marker([lat,lng], popup=my_location).add_to(myMap)
myMap.save("mylocation.html")