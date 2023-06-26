from pydub import AudioSegment
from pydub.playback import play
import random

def Turret_Deploy():
	nr = random.randint(1,6)
	str = "/home/mees/Portal-Turret/Portal Turret Voice Lines/Turret Turret Deploy {}.mp3"
	start = AudioSegment.from_file(str.format(nr))
	print(start)
	play(start)
	
def Turret_Pickup():
		nr = random.randint(1,10)
		str = "/home/mees/Portal-Turret/Portal Turret Voice Lines/Turret Turret Pickup {}.mp3"
		VL = AudioSegment.from_file(str.format(nr))
		print(VL)
		play(VL)
		
def Turret_Tipped():
		nr = random.randint(1,6)
		str = "/home/mees/Portal-Turret/Portal Turret Voice Lines/Turret Turret Tipped {}.mp3"
		VL = AudioSegment.from_file(str.format(nr))
		print(VL)
		play(VL)
