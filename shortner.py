import bitly_api

API_USER = "bitly username here"
API_KEY = "your api key here"
bitly = bitly_api.Connection(API_USER, API_KEY)
print("Do not enter prefix https://")
pre_input="https://"
try:
    user_input=input("Enter the url to be shortened : ")
    response = bitly.shorten(pre_input+user_input)
    print("Your short url is : ",response["url"])
except:
    print("Check & enter url again")
