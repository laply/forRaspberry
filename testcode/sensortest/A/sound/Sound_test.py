import numpy as np
import datetime
import MCP3208
# detect

class Control:
	def __init__(self, pin):
		self.sound_instance = MCP3208.MCP3208(pin)
		self.len = 30000

	def readSound(self):
		return self.sound_instance.analogRead()

	# conv analog data 
	def dataConvt(self):
		soundList = []

		for i in range(self.len):
			soundList.append(self.readSound())

		fft = np.fft.fft(soundList)/self.len
		fft = fft[range(int(self.len/2))]
		fft_m = abs(fft)
		readfft = []

		for i in range(0, len(fft_m)):
			if fft_m[i] > 0.5:
				readfft.append[i, fft_m[i]]
        # 1500 - 2100 :: 6000 - 8400
		return readfft