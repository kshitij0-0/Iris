from imageio import save
from keras.models import load_model
from time import sleep
from keras.utils import img_to_array
from keras.preprocessing import image
import cv2
import multiprocessing
import numpy as np
import time
from cProfile import run
from distutils import command
from email.mime import audio
from tkinter import NO
from pyparsing import re
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
from sys import argv
import random
from playsound import playsound
import pyjokes
from text_to_speech import speak
import requests
import multiprocessing
import time
from bs4 import BeautifulSoup
from keras.models import load_model
from time import sleep
from keras.utils import img_to_array
from keras.preprocessing import image
import cv2
import numpy as np




def talk(text):
   speak(text,"en",save=True,file='song.mp3', speak=True)




face_classifier = cv2.CascadeClassifier(r'emotions.xml')
classifier =load_model(r'model.h5')

emotion_labels = ['angry','','fear','happy','neutral', 'sad', 'surprise']

cap = cv2.VideoCapture(0)


count=0
emo=[]
while True:
        count+=1
        _, frame = cap.read()
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        faces = face_classifier.detectMultiScale(gray)

        for (x,y,w,h) in faces:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
            roi_gray = gray[y:y+h,x:x+w]
            roi_gray = cv2.resize(roi_gray,(48,48),interpolation=cv2.INTER_AREA)



            if np.sum([roi_gray])!=0:
                roi = roi_gray.astype('float')/255.0
                roi = img_to_array(roi)
                roi = np.expand_dims(roi,axis=0)

                prediction = classifier.predict(roi)[0]
                label=emotion_labels[prediction.argmax()]
                label_position = (x,y)
                cv2.putText(frame,label,label_position,cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
                emo.append(label)
            else:
                cv2.putText(frame,'No Faces',(30,80),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
        cv2.imshow('Emotion Detector',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
print(emo)
sc=max(set(emo), key = emo.count)
print(sc)
tex=("you are"+sc)


if 'sad' in tex:
        talk('you are so happy today, tell me y ?')
elif 'happy' in tex:
      talk('you are so happy today, tell me y ?')
      talk('you are so happy today, tell me y ?')
           
elif 'angry' in tex:
        talk('you look angry and serious, are u angry with me?')    
else:
        talk('you dont have any expression are u human?')    

cap.release()
cv2.destroyAllWindows()


