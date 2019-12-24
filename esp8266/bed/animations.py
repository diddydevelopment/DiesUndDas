

def animation1():
	n_rand = 10
	increment = 1
	current = 0
	last = 0
	max_col = 255
	bg_color = [0] * np.bpp
	color = [0] * np.bpp
	color[0] = max_col
	color_current = [0] * np.bpp
	color_current[1] = max_col
	color2 = [0] * np.bpp
	color2[2] = max_col
	while True:
		# np.fill(bg_color)
		# for j in range(n_rand):
		# 	np[randint(0,n)] = color2
		np[current] = color_current
		np[last] = color
		np.write()
		last = current
		current += increment
		if current <= 0 or current >= n-1:
			increment = increment * -1
			np.fill(bg_color)
		time.sleep_ms(100)


def animation2():
	time_till_change_ms = 60000
	increments_ms = 500
	max_intensity = (20,15,15,0)
	t = get_current_time()
	steps_made = 0
	current_color = ([randint(0,max_intensity[i]) for i in range(4)])
	next_color = ([randint(0,max_intensity[i]) for i in range(4)])
	color_increment = [(next_color[i]-current_color[i])/(time_till_change_ms/increments_ms) for i in range(len(current_color))]

	while True:
		if get_current_time()-t > increments_ms: #make step
			current_color = [current_color[i]+color_increment[i] for i in range(len(current_color))]
			np.fill([int(c) for c in current_color])
			np.write()
			print('changed color to ', current_color, 'goal color: ', next_color, 'color increment: ', color_increment)
			steps_made += 1
			t = get_current_time()
			time.sleep_ms(10)
			if steps_made >= time_till_change_ms/increments_ms:
				next_color = ([randint(0,max_intensity[i]) for i in range(4)])
				color_increment = [(next_color[i]-current_color[i])/(time_till_change_ms/increments_ms) for i in range(len(current_color))]
				steps_made = 0


def create_index_img(h,w,d,zigzack_top=True,zigzack_left=True,color_order=[1,0,2,3]):
	img = [[[0] * d for j in range(w)] for i in range(h)]
	for i in range(h):
		for j in range(w):
			for k in range(d):
				if i % 2 == 0:
					img[i][j][k] = (i*w*4) + j*4 + color_order[k]
				else: 
					img[i][w-j-1][k] = (i*w*4) + j*4 + color_order[k]
	return img
