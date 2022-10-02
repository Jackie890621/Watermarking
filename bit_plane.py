import numpy as np
from PIL import Image
from copy import deepcopy

Input = Image.open('input.jpg')
InputGray = Input.convert('L')

w, h = InputGray.size
input_arr = np.array(InputGray)
# print(input_arr)

mul = 1
for k in range(8):
	temp = np.zeros([h, w])
	for i in range(h):
		for j in range(w):
			if mul & input_arr[i][j]:
				temp[i][j] = 255

	# print(np_temp)
	mul *= 2
	output = Image.fromarray(np.uint8(temp))

	s = 'bit_plane/' + str(k + 1) + '_plane.jpg'
	output.save(s)