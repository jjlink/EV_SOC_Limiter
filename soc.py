#!/usr/bin/python
import os
import time
import json
from pprint import pprint
import datetime

# soc.bash
#rm soc.json
#curl  -X GET -c cookiejar https://tmc.openvehicles.com:6869/api/cookie\?username=XXXXX\&password=XXXXXXXX
#curl  -X GET -b cookiejar 'https://tmc.openvehicles.com:6869/api/charge/P-XXXXXX' >soc.json
#cat soc.json

# vera device ON - bash veraOn.sh
#curl -X GET http://192.168.1.104:3480/data_request?id=action\&output_format=json\&serviceId=urn:micasaverde-com:serviceId:HomeAutomationGateway1\&action=RunScene\&SceneNum=54

# vera device OFF - bash veraOFF.sh
#curl -X GET http://192.168.1.104:3480/data_request?id=action\&output_format=json\&serviceId=urn:micasaverde-com:serviceId:HomeAutomationGateway1\&action=RunScene\&SceneNum=55

target = 80



bashCommand = "rm nohup.out"
os.system(bashCommand)
bashCommand = "bash veraON.sh"
os.system(bashCommand)

while True:

    print("\n"+str(datetime.datetime.now())+"\n")
    bashCommand = "bash soc.sh"
    os.system(bashCommand)
 
    with open('soc.json') as data_file:   
    	data = json.load(data_file)
 
    #pprint(data)
 
    soc = int(data["soc"])
    chargestate = str(data["chargestate"])
 
    print("\nSOC= "+str(soc)+" Target= "+str(target)+"\n")

    if chargestate == "done" or chargestate == "stopped":
   	 print("Car is NOT charging.\n\n")
   	 bashCommand = "rm nohup.out"
   	 os.system(bashCommand)
   	 time.sleep((60 * 15))  # Delay for 15 minutes

    elif chargestate == "charging":
   	 if soc >= target:
   		 print("SOC is " + str(soc) + "%, Charge Limit of " + str(target) + "% Reached.\n")
   		 print("shut off power outlet.\n")
   		 bashCommand = "bash veraOFF.sh"
   		 os.system(bashCommand)
   		 bashCommand = "rm nohup.out"
   		 os.system(bashCommand)
   		 break
   		 #time.sleep((60 * 720))  # Delay for 12 hours.
   	 else:
   		 print("SOC is " + str(soc) + "%, Continue Charging to " +str(target) + "%\n")
   		 print("wait a while then go get more data from OVMS server.\n")
    else:
   	 print("Invalid jason file.")

   	 
    if (soc + 5) >= target:
    	time.sleep((15 * 1))  # Delay for 15 seconds
    else:
    	time.sleep((60 * 1))  # Delay for 1 minute

print('\nEnd of program.\n')
