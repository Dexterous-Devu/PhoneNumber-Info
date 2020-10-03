
__author__ : '@rockdevu'

import phonenumbers as ph     # pip install phonenumbers
from phonenumbers import carrier
from phonenumbers import geocoder

number = input("Enter Phone Number : ")
ch_number = ph.parse(number, None)
result_city = geocoder.description_for_number(ch_number, 'de')
ro_number = ph.parse(number, 'RO')
result_tele = carrier.name_for_number(ro_number, 'en')

print('Country : ', result_city)
print('Carrier : ', result_tele)
