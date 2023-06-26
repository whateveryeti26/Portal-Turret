from pydub import AudioSegment
from pydub.playback import play
from sense_hat import SenseHat
import random

sense = SenseHat()
sense.clear()

 
# ~ # for playing mp3 file
# ~ song = AudioSegment.from_file("/home/mees/Portal-Turret/Portal Turret Voice Lines/Turret Deploy.mp3", format="mp3")
# ~ print('playing sound using  pydub')
# ~ play(song)

while True:
	# get accelerometer readings
	raw = sense.get_accelerometer_raw()
	x = raw['x']
	y = raw['y']
	z = raw['z']
	
	x = float (round(x,1)) # vertical
	y = float (round(y,1))	
	z = float (round(z,1))
	print(f"x={x}, y={y},z={z}")
	if ((x < 0.8)and(y<0.3)and(z<0.3)):
		nr = random.randint(1,10)
		str = "/home/mees/Portal-Turret/Portal Turret Voice Lines/Turret Turret Pickup {}.mp3"
		VL = AudioSegment.from_file(str.format(nr))
		print(VL)
		play(VL)
