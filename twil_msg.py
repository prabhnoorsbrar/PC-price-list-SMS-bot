from twilio.rest import Client
#MAKE SEPERATE CONSTANT VARIABLE FILE CONTAINING AUTH TOKEN
import json
import automated
#import, open, and read JSON that contains twilio number and number that the message is being sent to
#IMPORTANT!!!! JSON IS EMPTY FILL WITH INFO FROM TWILIO CONSOLE OR ESLE THIS IMPORT IS POINTLESS
f = open('CONSTANTS.json')
data = json.load(f)
# Your Account SID from twilio.com/console
account_sid = data["ACC_SID"]
# Your Auth Token from twilio.com/console
auth_token  = data["AUTH_TKN"]

client = Client(account_sid, auth_token)
price= []
#scrape website via automated module
price = automated.scrape_pc_picker()
#Twilio code-block for sending SMS
message = client.messages.create(
    #My num IS THE NUMBER YOU DESIRE TO SEND SMS ALERTS TO
    to=data["MY_NUM"], 
    #TWIL NUM IS THE NUMBER YOU CAN GET FROM TWILIO
    from_=data["TWIL_NUM"],
    #screenshot of price list (VARIES USER TO USER, YOU CAN INCLUDE YOUR OWN SCREESNSHOT) to make SMS more user friendly
    media_url=['https://i.gyazo.com/046ccc1db8827352e92133d1d9fe97c7.png'],
    body=("Today's total price of the PC parts listed above are " + price[len(price)-1]))
#prints message id from twilio to confirm success of message sent
print(message.sid)