# from PIL import Image
import cv2
import numpy as np
import firebase_admin
from firebase import firebase
import firebase
from firebase_admin import db
import pyrebase
import pytesseract
from googletrans import Translator
translator = Translator()
import firebase_admin
from firebase import firebase
from firebase_admin import db
import speech_recognition as sr
import os
from googletrans import Translator
from gtts import gTTS
from PIL import Image
import cv2
import pytesseract
import requests

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
firebased = firebase.FirebaseApplication("https://janaparvani-default-rtdb.firebaseio.com/",None)




config = {
  "apiKey": "AIzaSyBpFXSVnSTFMUcMyqhg7YUBJMdPhKl43B0",
  "authDomain": "janaparvani.firebaseapp.com",
  "databaseURL": "https://janaparvani-default-rtdb.firebaseio.com",
  "projectId": "janaparvani",
  "storageBucket": "janaparvani.appspot.com",
  "messagingSenderId": "642181219649",
  "appId": "1:642181219649:web:71c8d5ca4d1d7904ba8dc0",
  "measurementId": "G-47FWF9RELL"
}

firebase = pyrebase.initialize_app(config)
while True:
    f = firebased.get('OCR', '') 
    item = f.items()


    for key, val in f.items():
        to_lang = (val["to_lang"])
        # user = (val["User"])
    # to_lang = "Hindi"


    firebase = pyrebase.initialize_app(config)
    storage = firebase.storage()
    image_ref = storage.child("images/a.jpg")
    url = image_ref.get_url(None)
    img = requests.get(url).content


    # To display image

    # img = np.array(bytearray(img), dtype=np.uint8)
    # img = cv2.imdecode(img, cv2.IMREAD_UNCHANGED)

    # cv2.imshow("Image", img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    # to save image in local storage
    # with open("a.jpg", "wb") as f:
    #     f.write(img)


    # img = cv2.imread('C:\\Users\\subra\\OneDrive\\Desktop\\ocrhojao\\hi.jpg')



    img = np.array(bytearray(img), dtype=np.uint8)
    img = cv2.imdecode(img, cv2.IMREAD_UNCHANGED)


    img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    # print(type(img))


    text =pytesseract.image_to_string(img)
    translation = translator.translate(text, dest=to_lang)
    x = translation.text
    org = text
    trans=x
    print(to_lang )
    print(org)
    firebased.put('/OCR/A','Org_text',text)
    firebased.put('/OCR/A' ,'trans_text',x)