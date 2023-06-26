from sense_hat import SenseHat
sense = SenseHat()
def AccelerometerReadings():
		raw = sense.get_accelerometer_raw()
		x = raw['x']
		y = raw['y']
		z = raw['z']
		
		x = float (round(x,1)) # vertical
		y = float (round(y,1))	
		z = float (round(z,1))
		print(f"x={x}, y={y},z={z}")
		return x, y , z
		
