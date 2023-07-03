from sense_hat import SenseHat
import time
import RPi.GPIO as GPIO

sense = SenseHat()
GPIO.setmode(GPIO.BCM)

trig_pin = 17
echo_pin = 27

GPIO.setup(trig_pin, GPIO.OUT)
GPIO.setup(echo_pin, GPIO.IN)

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
		
def UltrasonicDistanceSensor():
	GPIO.output(trig_pin, GPIO.HIGH)
	time.sleep(0.00001)
	GPIO.output(trig_pin, GPIO.LOW)
	
	GPIO.wait_for_edge(echo_pin, GPIO.RISING)
	pulse_start = time.time()
	
	GPIO.wait_for_edge(trig_pin, GPIO.FALLING)
	pulse_end = time.time()
		
	pulse_duration = pulse_end - pulse_start
	distance = pulse_duration * 17150  # Speed of sound = 343 m/s
	distance = round(distance, 2)
	return distance
