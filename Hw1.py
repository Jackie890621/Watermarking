import numpy as np
import sys
import os
from PIL import Image, ImageOps
from copy import deepcopy

def watermark(Input, water, num, w, h):
	for i in range(h):
		for j in range(w):
			Input[i][j] -= (Input[i][j] % (2 ** num))
			temp = num
			count = 1
			while temp > 0:
				if water[i][j] & (128 // count):
					Input[i][j] += (2 ** (temp - 1))
				count *= 2
				temp -= 1
	output = Image.fromarray(Input, 'L')
	s = 'result/output_' + str(num) + '.png'
	output.save(s)

def dewatermark(Input, num, w, h):
	water = np.zeros([h, w])
	for i in range(h):
		for j in range(w):
			temp = num
			count = 1
			while temp > 0:
				if Input[i][j] & (2 ** (temp - 1)):
					water[i][j] += 128 // count
				count *= 2
				temp -= 1
	# print(water)
	water = np.uint8(water)
	output = Image.fromarray(water, 'L')
	s = 'result/output_' + str(num + 3) + '.png'
	output.save(s)

if __name__ == '__main__':
	if len(sys.argv) < 2:
		print('You should select input and watermark')
		sys.exit()

	Input = Image.open(sys.argv[1])
	water = Image.open(sys.argv[2])
	
	InputGray = Input.convert('L')
	waterGray = water.convert('L')

	# InputGray.save('input_gray.png')
	# waterGray.save('watermark_gray.png')

	w, h = InputGray.size
	input_arr = np.array(InputGray)
	water_arr = np.array(waterGray)

	# os.mkdir('result')

	for i in range(1, 4):
		watermark(input_arr, water_arr, i, w, h)
		s = 'result/output_' + str(i) + '.png'
		result = Image.open(s)
		result_arr = np.array(result)
		dewatermark(result_arr, i, w, h)
	