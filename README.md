# EV_SOC_Limiter
 OVMS stop charging EVSE at 80% OVMS stop charging EVSE at 80%

http://myimiev.com/forum/viewtopic.php?f=25&t=1786&start=80

 Post subject: Re: OVMS for Mitsubishi i-Miev, Citroen C-Zero and Peugeot iPostPosted: Sat Feb 13, 2016 9:38 am
	
pbui19 wrote:
PV1 wrote:
I was reading on the Tesla forum that the OVMS has the capability to stop charge at either a desired range or a SOC. Have you or anyone else tried to get the i-MiEV to stop charge at 80%, for example? 

I gather daily readings of usage, distance, HVAC usage, etc. Currently, the best (most accurate) way to gather daily usage info is to allow the car to fully charge everyday, so that ending SoC is the same. I would like the capability to automatically stop charge at a lower SoC, say 85-90% to extend the life of my battery.

Here's the page on the Tesla forum:
http://www.teslamotorsclub.com/showthread.php/6754-Open-Vehicle-Monitor-System-(OVMS)-Technical-Discussion/page8Add to Google Calendar


was there an answer to PV1's question about OVMS ability to stop charge at a selectable SOC % ?


Here is how I did this for home use (not remote use) with a Intermatic CA3750 Z-wave device, and a VeraLite Home Controller, and a BeagleBone Black Single Board Computer.

I purchased a Intermatic CA3750 to shut off my electric car charger when the charge reaches a certain percentage (like 80%). Many thanks to the previous reviewers of the Intermatic CA3750 on Amazon.com for clarifying how to wire this unit up for electric water heaters; the wiring is the same for an electric car EVSE. I simply wrote a Python program to read the charging status and state of charge percentage from the OpenVehicles.com server. So when the car is charging the Python program watches to see when the car is charging and when the state of charge reaches say 80%; it then sends a Http request to my VeraLite Home Controller which sends a Z-wave signal to the CA3750 and shuts off the power to the car charging unit. The python program runs on a BeagleBone Black Single Board Computer Development Board I had laying around doing nothing. This set up works really nice and I already had all the parts except for the Intermatic CA3750. Plus I learned Python in a very short time and love its ease of use.

Intermatic CA3750 InTouch Wireless Multi-Volt 120-277VAC Contactor Module by Intermatic
Link: http://www.amazon.com/Intermatic-CA3750 ... B000YUCES2
Link: http://store.homeseer.com/store/Interma ... -P407.aspx
Link: http://www.smarthome-products.com/p-331 ... odule.aspx

Wiring diagrams:
Link: http://waterheatertimer.org/How-to-wire ... A3750.html 

Mi Casa Verde VeraLite Home Controller, White and Green by Mi Casa Verde
Link: http://www.amazon.com/Mi-Casa-Verde-Ver ... Controller

BeagleBone Black Rev C (4G) Single Board Computer Development Board
Link: http://www.amazon.com/BeagleBone-Black- ... C+%284G%29

Python program Link:
http://bit.ly/OVMS_EVSE_80_Percent
_________________
John - 2012 Silver i-MiEV SE model, Jan 19th, 2012 w/OpenEvse, caniOn,& OVMS. 
