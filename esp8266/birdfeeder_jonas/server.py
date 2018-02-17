import alarm

def loadPage(name):
    html="<h1><a href='.'>Error!</a></h1>"
    try:
        f = open(name)
        html=f.read()
        f.close()
    except MemoryError as e:
        print("Error loading html text: "+str(e))
    
    return html


def updatePage(html):
    import machine
    #add current time to html
    currentTime=machine.RTC().datetime()
   
    #add current alarms to html
    alarmDates=alarm.loadAlarms()

    idDays={0:'Monday',1:'Tuesday',2:'Wednesday',3:'Thursday',4:'Friday',5:'Saturday',6:'Sunday'}

    alarmText=""
    for date in alarmDates:
        alarmText+="<option>"+ idDays[date[0]]+" "+ '{:02}'.format(date[1]) +":"+ '{:02}'.format(date[2]) +"</option>"

    r="<h1><a href='.'>Error!</a></h1>"
    try:
        r=html.format(currentTime[2],currentTime[1],currentTime[0],idDays[currentTime[3]],'{:02}'.format(currentTime[4]),'{:02}'.format(currentTime[5]),alarmText)
    except (MemoryError,KeyError) as e:
        print("Error formatting response: "+str(e))
        
    return r
    

def start():
    import socket
    
    while True:
        s, cl = None, None
        addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
        
        print("server: waiting for request")
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            
            # A port on which a socket listened remains inactive during some time.
            # This means that if you run this sample, terminate it, and run again
            # you will likely get an error. To avoid this timeout, set SO_REUSEADDR
            # socket option.
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            s.bind(addr)
            s.listen(1)

            #wlan = network.WLAN(network.STA_IF)
            #print('HTTP waiting on ip:', wlan.ifconfig()[0],'port:', 80 )

            req=""
            agent=""
            cl, addr = s.accept()
        except OSError as e:
            print('Error while creating socket: '+str(e))
            if cl is not None:
                cl.close()
            if s is not None:
                s.close()
            continue
        
        print('client connected from', addr)
        cl_file = cl.makefile('rwb', 0)
        
        while True:
            line = cl_file.readline()
            
            if(b'GET' in line):
                req=str(line)
            elif(b'User-Agent' in line):
                agent=str(line)
            
            if not line or line == b'\r\n':
                break
                
        if 'birdy.svg' in req:
            data=b''
            try:
                f = open("birdy.svg", "rb")
                data=f.read()
                f.close()
            except MemoryError as e:
                print("Error loading image: "+str(e))
            
            header= "HTTP/1.1 200 OK\r\n Content-Type: image/svg+xml\r\n Content-Length: "+ str(len(data)) +"\r\n\r\n"
            
            try:
                cl.sendall(header)
                cl.sendall(data)
            except OSError as e:
                print('Error while sending response: '+str(e))
                
            del header #important to free memory!
            del data #important to free memory!
            cl.close()
            s.close()
        else: 
            params=dict()
            
            try:
                for p in req.split('?')[1].split('&'):
                    r=p.split('=')
                    params.setdefault(r[0], []).append(r[1])
            except:
                 params={}
                
            if 'feed' in params:
                print('server: do feeding')
            if 'syncTime' in params:
                print('server: syncing time')
                alarm.ntpSetTime()
            if 'save' in params or 'activate' in params:
                print('server: setting new alarms')
               
                days={'Monday':0,'Tuesday':1,'Wednesday':2,'Thursday':3,'Friday':4,'Saturday':5,'Sunday':6}

                dates=[]
                try:
                    for time in params['alarmDates']:
                        day,clock=time.split('+')
                        hour,minute=clock.split('%3A')
                        weekday=days[day]
                        dates.append((int(weekday),int(hour),int(minute)))
                except:
                    print("No alarm dates set!")
                print('server: Saving alarms: '+str(dates))
                alarm.saveAlarms(dates)
               
            if 'activate' in params:
                response = "<h1>Going to sleep...zzz</h1>"
            else:
                if any(s in agent for s in ('Android','webOS','iPhone','iPad','iPod','BlackBerry','IEMobile','Opera Mini')):
                    response = updatePage(loadPage('feeder_mobile.html'))
                else:
                    response = updatePage(loadPage('feeder.html'))
            
            try:
                cl.sendall(response)
            except OSError as e:
                print('Error while sending response: '+str(e))
            
            del response #important to free memory!
            cl.close()
            s.close()
                
            if 'activate' in params:
                alarm.manualStart()
           
