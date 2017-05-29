#!/usr/bin/env python
# -*-coding:utf-8 -*-
import os
import speech_recognition as sr
import time
import datetime
startTime = datetime.datetime.now()
i = 1
apiCredential = {
  "url": "https://stream.watsonplatform.net/speech-to-text/api",
  "username": "xxxxx",
  "password": "xxxx"
}
audioDir = 'audio'
textDir = 'text'
for name in os.listdir(audioDir):
    print("%d %s transforming..." % (i, name))
    r = sr.Recognizer()
    try:
        with sr.WavFile(audioDir + '/' + name) as source:
            audio = r.record(source)
            IBM_USERNAME = apiCredential['username']
            IBM_PASSWORD = apiCredential['password']
            text = r.recognize_ibm(audio, username=IBM_USERNAME, password=IBM_PASSWORD, language='en-US')
            print(text)
            open(textDir + '/' + name, 'a+').write(text)
            time.sleep(5)
            tempTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print('%s %d %s finished.' % (tempTime, i, name))

    except Exception as e:
        print(e)
        tempTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print('%s %d %s failed.' % (tempTime, i, name))
        continue
endTime = datetime.datetime.now()
last = endTime - startTime
print('Time used： %s' % last)


