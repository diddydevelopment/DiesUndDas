num_motors = 4
amp_per_motor = 8
bias = 5
weight_without_battery = 373
pull = 400
total_amps_needed = amp_per_motor * num_motors + bias
weight_factor = 0.7

max_weight = weight_factor * (num_motors*pull)


print("Total copter weight should be under "+str(max_weight)+" grams")
print("Battery can weight up to "+str(max_weight-weight_without_battery))
print("")
print("Battery configuration")
for ma in range(500,6000,100):
	for c in range(10,100,5):
		a = ma / 1000
		if a*c > total_amps_needed:
			print("Ah = "+str(a)+" and C = "+str(c)+" should fit well")
			break
