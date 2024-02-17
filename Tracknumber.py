import phonenumbers
from phonenumbers import geocoder

phone_number1 = phonenumbers.parse("+2389798713", None)
phone_number2 = phonenumbers.parse("+2389537312", None)
phone_number3 = phonenumbers.parse("+2385923142", None)
phone_number4 = phonenumbers.parse("+2389545259", None)

print("\nPhone numbers Location")
print(geocoder.description_for_number(phone_number1,"en"))
print(geocoder.description_for_number(phone_number2,"en"))
print(geocoder.description_for_number(phone_number3,"en"))
print(geocoder.description_for_number(phone_number4,"en"))


