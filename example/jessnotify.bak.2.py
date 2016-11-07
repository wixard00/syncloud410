#jessnotify: para enviar sms desde visualfac
#from twilio.rest import TwilioRestClient
#import os
#import datetime
## Download the twilio-python library from http://twilio.com/docs/libraries
## Find these values at https://twilio.com/user/account
## -*- encoding: utf-8 -*-
#os.system("CLS")
#print(os.getcwd())
#c=raw_input("Ingrese mensaje a enviar a +593994367340 :")
##c="Mensaje de prueba %s" % datetime.datetime.now()

#ACCOUNT_SID = "AC8eb732322f5ce63c6b7f3a6b08defa44"
#AUTH_TOKEN = "910cce818d98f078d72ee23821ee861f"

#client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)

#try:
	#message=client.messages.create(to="+593994367340",from_="+12014312530",body=c,)
#except:
	#print("Ocurrio un error al momento de enviar el mensaje")
#message=client.messages.create(to="+593994367340",from_="+12014312530",body=c,)
#print (message.sid)


import textmagic.client
client = textmagic.client.TextMagicClient('angel.ordonez', 'IJ0gJ7lz0R')
mensaje=raw_input("Ingrese mensaje: ")
numero_mobil=raw_input("")
result = client.send(mensaje, "593994367340")
message_id = result['message_id'].keys()[0]

response = client.message_status(message_id)
status = response[message_id]['status']

print (response)
print (status)