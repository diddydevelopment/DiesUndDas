def sendTx(sendCharASCII):
	sendByte = '{0:b}'.format(sendCharASCII).zfill(8)
	sendByte = sendByte[::-1]
	print(sendByte)
	sendByteInt = [int(bit) for bit in sendByte]
	gpio.output(tx,0)
	mySleep(baud)
	
	sendO = []
	last0 = True
	repeat = 1.0
	
	for sb in sendByte:
		if sb == '0':
			if last0 == True:
				repeat = repeat +1
			if last0 == False:
				sendO.append((gpio.HIGH,repeat))
				repeat = 1.0
				last0 = True
		else:
			if last0 == False:
				repeat = repeat +1
			if last0 == True:
				sendO.append((gpio.LOW,repeat))
				repeat = 1.0
				last0 = False
	if last0:
		sendO.append((gpio.LOW,repeat))
	else:
		sendO.append((gpio.LOW,repeat))

	print(sendO)
	print('\n')
	for bit in sendO:
		#print('sending ',bit)
		gpio.output(tx,gpio.HIGH)
		mySleep(bit[1]*baud)
	gpio.output(tx,gpio.PULLUP)
	mySleep(0.01)
