#This progam uses high-precision timestamps to generate
#unique identifying numbers.

#These numbers will be used to identify individual facilities and orders.

#imports
import time

#make sure movearray is empty and then add a timestamp to it
timestamp = []
when = time.time()
when = str(when)
timestampstringlength = len(when)
if(timestampstringlength < 15):
    for x in range(0, (15 - timestampstringlength)):
        when = when + "0"
timestamp.append(when)
print(timestamp, "\n")
