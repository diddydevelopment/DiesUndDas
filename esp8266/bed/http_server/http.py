debug_mode = False

def dbg(message):
	global debug_mode
	if debug_mode:
		print(message)

def http_listen():
	import machine
	import socket
	import ure


	response_header = "HTTP/1.x [status_code] OK\r\nContent-Type: text/html; charset=UTF-8\r\n\r\n"

	addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
	socket_obj = socket.socket()
	socket_obj.bind(addr)
	socket_obj.listen(1)

	dbg('listening on '+ str(addr))


	while True:
		client, addr = socket_obj.accept()
		try:
			dbg('client connected from '+ str(addr))
			client.setblocking(False)

			status_code = 200
			request = b""
			while True:
				try:
					chunk = client.recv(512)
					request += chunk
				except OSError:
					break
			dbg('request: '+ str(request))
			if "HTTP" not in request:
				client.close()
				continue

			request_str = request.decode('utf-8')
			request_str_fileline = request_str[:request_str.find('\r\n')]
			request_method = ''
			if request_str_fileline[:3] == 'GET':
				request_method = 'GET'
				request_file_vars = request_str_fileline[4:request_str_fileline.find('HTTP')-1]
			elif request_str_fileline[:4] == 'POST':
				request_method = 'POST'
				request_file_vars = request_str_fileline[5:request_str_fileline.find('HTTP')-1]
			else:
				client.close()
				continue

			get = dict()
			if '?' in request_file_vars:
				vars_begin = request_file_vars.find('?')
				request_file = request_file_vars[:vars_begin]
				get = dict(tuple(tuple([x[:x.find('=')],x[x.find('=')+1:]]) for x in request_file_vars[vars_begin+1:].split('&')))
			else:
				request_file = request_file_vars
			post = dict()
			vars = request_str[request_str.find('\r\n\r\n')+4:]
			if vars != '':
				post = dict(tuple(tuple([x[:x.find('=')],x[x.find('=')+1:]]) for x in vars.split('&')))

			dbg(request_method)
			dbg(request_file)
			dbg(get)
			dbg(post)

			try:
				fh = open(request_file,'r')
				content = fh.read()
			except:
				content = 'Can not find page, maaaaan'
				status_code = 404
			#loc_vars = locals()
			#print('loc vars: '+str(loc_vars))
			while '[py]' in content and '[/py]' in content:
				start = content.find('[py]')
				end = content.find('[/py]')
				code = content[start + 5:end]
				rtn = ''
				_locals = {'request_method': request_method, 'request_file': request_file, 'get': get, 'post': post, 'rtn': rtn}
				exec(code,globals(),_locals)
				rtn = _locals['rtn']
				content = content[:start] + str(rtn) + content[end + 6:]

			response = response_header.replace('[status_code]',str(status_code))+content
			client.send(response)
		except Exception as e:
			dbg('--- There was something wrong in you page file ---')
			import sys
			sys.print_exception(e)
			dbg('------------------------------------')
		client.close()
	socket_obj.close()
