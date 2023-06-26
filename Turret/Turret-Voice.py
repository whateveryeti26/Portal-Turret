from pydub import AudioSegment
from pydub.playback import play
from sense_hat import SenseHat

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
	
	x = float (round(x,1))
	y = float (round(y,1))
	z = float (round(z,1))
	print(f"x={x}, y={y},z={z}")
	
