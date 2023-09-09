import phonenumbers

import opencage
from track import num
from phonenumbers import geocoder
pepnumber=phonenumbers.parse(num)
location=geocoder.description_for_number(pepnumber,"en")
print(location)
service_provider=phonenumbers.parse(num)
from phonenumbers import carrier
print(carrier.name_for_number(service_provider,"en"))

from opencage.geocoder import OpenCageGeocode
key='7cd04a85da16478bb79f524d5946c687'
geocoder=OpenCageGeocode(key)
query=str(location)
results=geocoder.geocode(query)
#print (results)
lat=results[0]['geometry']['lat']
lng=results[0]['geometry']['lng']
print ("latitude = ",lat)
print("longitude ", lng)
