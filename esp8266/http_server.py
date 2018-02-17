import machine


html = """<!DOCTYPE html>
<html>
    <head> <title>Automative intelligent budgie feeder machine</title> </head>
    <body> <h1>Please feed budgie regularely for happy budgie</h1>
	<form method="POST" action="">
	<input type="submit" name="feed" value="feed budgie">
	</form>
    </body>
</html>
"""

import socket
addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]

s = socket.socket()
s.bind(addr)
s.listen(1)

print('listening on', addr)

while True:
    do_feed = False
    cl, addr = s.accept()
    print('client connected from', addr)
    cl_file = cl.makefile('rwb', 0)
    while True:
        line = cl_file.readline()
        if 'feed=' in line:
            do_feed = True
        if not line or line == b'\r\n':
            break
    response = html
    cl.send(response)
    cl.close()
    if do_feed:
        print('do feeding')