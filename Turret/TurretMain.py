from TurretVoiceFunctions import *
from TurretSensorReadings import *
import random
import time
Turret_Deploy()
last_tipped_time = 0
tipped_timer = 5
while True: 
	current_time = time.time()
	x, y , z = AccelerometerReadings() # from TurretSensorReadings
	if ((0<x<=0.9)and(0<y<0.3)and(-0.5<z<0.3)):
		Turret_Pickup()
	elif ((x<0.3)and(-0.5<y>0.5)or(-0.5<z>0.5)):
		if current_time - last_tipped_time>=tipped_timer:
			 Turret_Tipped()
			 last_tipped_time = current_time
