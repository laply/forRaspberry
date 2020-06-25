import datetime
import MCP3208
# detect

class Control:

	def __init__(self, pin):
		self.sound_instance = MCP3208.MCP3208(pin)


	# conv analog data 
	def dataConvt(self):
		read = self.sound_instance.analogRead()

		print(read)
		if read > 300 :
			return True
		else :
			return False
