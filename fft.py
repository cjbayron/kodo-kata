''' Cooley-Tukey FFT algorithm implementation
'''
import math

def fft(signal):
	# check signal length
	nbits = math.log2(len(signal))
	if nbits != int(nbits):
		raise Exception("Signal length must be a power of 2") 

	# re-arrange signal elements by reversing bits
	nbits = int(nbits)
	arr_sig = [] # re-arranged signal
	for i in range(len(signal)):
		bin_str = ('{:0%db}' % nbits).format(i)
		idx = int(bin_str[::-1], 2)
		arr_sig.append(signal[idx])

	# perform DFT by butterfly method
	print(arr_sig)

if __name__ == "__main__":
	signal = [0.707, 1, 0.707, 0, -0.707, -1, -0.707, 0]
	fft(signal)