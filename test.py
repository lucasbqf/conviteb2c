import time
import requests
import random
import threading

api_url = "http://54.196.253.71:5001/"


def testIndex():
    while True:
        response = requests.get(api_url)
        print(response)

def testCreateinvite ():
    x = 0
    while x<20:
        invited = random.randint(-99999999999,99999999999)
        inviter = random.randint(-99999999999,99999999999)
        print(invited)
        print(inviter)
        json = {"invited_user_id":invited,"user_id":inviter}
        response =  requests.post(api_url+"/create_invite",json=json)
        print(response)
        x += 1
    print("thread finalizada")

class threadCreateInvite(threading.Thread):
    def run(self):
        testCreateinvite()
    
        

threads = []
for x in range(0,50):
    threads.append(threadCreateInvite())

for thread in threads:
    thread.start()

print("isso ai")