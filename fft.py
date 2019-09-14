''' Cooley-Tukey FFT algorithm implementation
'''
import math
import numpy as np


def compute_w(k, n):
	''' Compute omegas: e^(-j*2*pi*k/n)

	let theta = 2*pi*k/n
	e^(-j*theta) = cos(theta) - j*sin(theta)
	'''
	theta = 2*np.pi*k/n
	# compute real and imaginary parts
	w = np.cos(theta) + (-1j) * np.sin(theta)

	return w


def dft(signal):
	''' Discrete fourier transform on signals with length 2^k
	'''
	N = len(signal)

	res = [0] * N
	for i in range(int(N/2)):
		rx = i 			      # index for real component
		jx = int(i + (N/2))	  # index for imaginary component
		w = compute_w(i, N)   # sinusoidal component

		res[rx] = signal[rx] + w*signal[jx]
		res[jx] = signal[rx] - w*signal[jx]

	return res


def fft(signal):
	''' Cooley-Tukey algorithm
	'''
	# check signal length
	N = len(signal)
	nbits = math.log2(N)
	if nbits != int(nbits):
		raise Exception("Signal length must be a power of 2") 

	# re-arrange signal elements by reversing bits
	nbits = int(nbits)
	arr_sig = [] # re-arranged signal
	for i in range(N):
		bin_str = ('{:0%db}' % nbits).format(i)
		idx = int(bin_str[::-1], 2)
		arr_sig.append(signal[idx])

	# perform DFT by butterfly method
	for stage in range(1, nbits+1):
		num_dfts = 2**(nbits-stage)
		num_sigs = int(N / num_dfts)
		for set_ix in range(num_dfts):
			ix = set_ix * num_sigs
			arr_sig[ix:ix+num_sigs] = dft(arr_sig[ix:ix+num_sigs])

	return arr_sig


if __name__ == "__main__":
	signal = [0.707, 1, 0.707, 0, -0.707, -1, -0.707, 0]
	print("Input: ", signal)
	print("Output: ", fft(signal))