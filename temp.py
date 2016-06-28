import os
import time 

def getCPUtemperature():
	res = os.popen('vcgencmd measure_temp').readline()
	return(res.replace("temp=","").replace("'C\n",""))
	
	temp = float(getCPUtemperature())

print "CPU Temperature (Celsius): "
print (getCPUtemperature())
