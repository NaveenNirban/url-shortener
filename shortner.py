import bitly_api

API_USER = "naveennirban"
API_KEY = "R_583061bd02004cd6af21af95b7c93839"
bitly = bitly_api.Connection(API_USER, API_KEY)
print("Do not enter prefix https://")
pre_input="https://"
try:
    user_input=input("Enter the url to be shortened : ")
    response = bitly.shorten(pre_input+user_input)
    print("Your short url is : ",response["url"])
except:
    print("Check & enter url again")