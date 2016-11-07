# -*- encoding: utf-8 -*-
#jessnotify: para enviar sms desde visualfac
import textmagic.client
import os
os.system("CLS")

client = textmagic.client.TextMagicClient('angel.ordonez', 'IJ0gJ7lz0R')
mensaje=raw_input("Ingrese mensaje: ")
numero_mobil=raw_input("Ingrese el telefono: ")
result = client.send(mensaje, "593994367340")
message_id = result['message_id'].keys()[0]

response = client.message_status(message_id)
status = response[message_id]['status']

print (response)
print (status)