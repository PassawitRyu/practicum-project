import requests
import os
from time import sleep
url = 'https://notify-api.line.me/api/notify'
token = 'bmXDs79Q79lBkS61HotGQ0HGDyt0QD63ibnaB23TRvV'
headers = {'content-type':'application/x-www-form-urlencoded','Authorization':'Bearer '+token}
send = False

file = open('./usb-example/python/now.txt').read()
# print(file)

while True:
    if open('./usb-example/python/now.txt').read() == '1 0 0' or open('./usb-example/python/now.txt').read() == '1 0 1' or open('./usb-example/python/now.txt').read() == '1 1 0' :
        if send == False:
            r1 = requests.post(url, headers=headers, data={'message': 'อย่าลืมเก็บของลงกล่องด้วยนะ'})
            r2 = requests.post(url, headers=headers, data={'message': 'Do not forget to put your stuff in the boxs.'})
            print(r1,r2)
            send = True
    elif open('./usb-example/python/now.txt').read() == '2 1 1':
        if send == False:
            r1 = requests.post(url, headers=headers, data={'message': 'คุณลืมของไว้ที่ห้อง !!'})
            r2 = requests.post(url, headers=headers, data={'message': 'Do not forget your stuff !'})
            print(r1,r2)
            send = True
    elif open('./usb-example/python/now.txt').read() == '2 1 0':
        if send == False:
            r1 = requests.post(url, headers=headers, data={'message': 'คุณลืมกระเป๋าสตางค์หรือเปล่า ?'})
            r2 = requests.post(url, headers=headers, data={'message': 'Did your forget your wallet ?'})
            print(r1,r2)
            send = True
    elif open('./usb-example/python/now.txt').read() == '2 0 1':
        if send == False:
            r1 = requests.post(url, headers=headers, data={'message': 'คุณจะเอานาฬิกาไปด้วยไหม ?'})
            r2 = requests.post(url, headers=headers, data={'message': 'Will you bring your watch ?'})
            print(r1,r2)
            send = True
    else:
        send = False
    sleep(1)









# while 1:
#     print(os.environ.get('ryu'))
#     if os.environ.get('ryu') == '11':
#         if send == False :
#             r1 = requests.post(url, headers=headers, data={'message': 'Helloooooo'})
#             print(r1.text)
#             send = True
#     else:
#         send = False

# r2 = requests.post(url, headers=headers, data={'message': 'Do not forget your stuff !'})

#msg1 = 'คุณลืมของนะ'
#msg2 = 'กลับไปเอาของที่ลืมไว้ด้วยล่ะ'

#r1 = requests.post(url, headers=headers, data = {'message':msg1})
#r2 = requests.post(url, headers=headers, data = {'message':msg2})

#print (r1.text)
#print (r2.text)