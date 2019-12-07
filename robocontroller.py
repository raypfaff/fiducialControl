import json
import zmq
import requests
import time
from time import sleep

context = zmq.Context()

#  Socket to talk to server
socket = context.socket(zmq.REP)
socket.connect("tcp://localhost:5555")
while True:
   message = socket.recv_string()
   id_list={}
   socket.send(b"x")
   jsonValues=json.loads(message)
   print(jsonValues)
   dist=jsonValues['z']
   if dist>1.5 :
      if jsonValues['id'] not in id_list :
         # Don't return to an id you went to already
         # I really should make this a function call
         if jsonValues['x']/jsonValues['z']>.24 :
            print ('turning right')
            r = requests.get('http://{IP}//rev.cgi?Cmd=nav&action=18&drive=6&speed=6', auth=('admin', 'admin1'))
         elif jsonValues['x']/jsonValues['z']<-.24 :
            print ('turning left')
            r = requests.get('http://{IP}//rev.cgi?Cmd=nav&action=18&drive=5&speed=6', auth=('admin', 'admin1'))
         r = requests.get('http://{IP}//rev.cgi?Cmd=nav&action=18&drive=1&speed=4', auth=('admin', 'admin1'))
         r = requests.get('http://{IP}//rev.cgi?Cmd=nav&action=18&drive=1&speed=4', auth=('admin', 'admin1'))
         r = requests.get('http://{IP}//rev.cgi?Cmd=nav&action=18&drive=0&speed=9', auth=('admin', 'admin1'))
         sleep(.5)
      else :
         print('Found this ID already')
         r = requests.get('http://{IP}//rev.cgi?Cmd=nav&action=18&drive=5&speed=6', auth=('admin', 'admin1'))
         r = requests.get('http://{IP}//rev.cgi?Cmd=nav&action=18&drive=0&speed=9', auth=('admin', 'admin1'))
         sleep(.5)
   elif dist <= 1.5 and dist >0 :
      print("found goal")     
      id_list[jsonValues['id']]=1
      # Start searching for next id
   else :
      print("lost tag or searching for next one")
      r = requests.get('http://{IP}//rev.cgi?Cmd=nav&action=18&drive=5&speed=6', auth=('admin', 'admin1'))
      r = requests.get('http://{IP}//rev.cgi?Cmd=nav&action=18&drive=0&speed=9', auth=('admin', 'admin1'))
      sleep(.5)
