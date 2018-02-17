import machine

def loadAlarms():
    alarmDates=[]
    try:
        with open("alarms.dat") as f:
            alarmDates = eval(f.read())
    except:
        print("Failed opening alarms.dat")
    return alarmDates
    

def saveAlarms(data):
    try:
        with open("alarms.dat", "w") as f:
            f.write(repr(data))
    except:
        print("Failed writening to alarms.dat")

def triggerSleep():
    print('Im tired...going into deepsleep')
    # put the device to sleep
    machine.deepsleep()
    

def setSleep(sec):
    rtc = machine.RTC()
    rtc.irq(trigger=rtc.ALARM0, wake=machine.DEEPSLEEP)
    rtc.alarm(rtc.ALARM0, sec*1000)


def dateToSec(date):
    return date[0]*86400+date[1]*3600+date[2]*60

def calcDiffDates(dateA,dateB):
    sec=dateToSec(dateB)-dateToSec(dateA)
    if(sec<0):
        sec=(604800-dateToSec(dateA))+dateToSec(dateB)
    return sec
        
def checkTimeToAlarm():
    rtc = machine.RTC()
    currentTime=rtc.datetime()
    
    nextTime=(7,24,60)
    firstInWeek=(7,24,60)
    thisWeek=False
    
    alarmDates=loadAlarms()
    
    if(len(alarmDates)<1):
        return -1 #no alarms set
    
    for date in alarmDates:
        if(date<firstInWeek):
            firstInWeek=date
        #search for next alarm after current time and before last found next alarm
        if(date>=currentTime[3:6] and date<nextTime):
                nextTime=date
                thisWeek=True
    
    #check if next alarm lies in next week
    if(thisWeek==False):
        nextTime=firstInWeek
           
    nextAlarm=nextTime
    
    #check if correct week, weekday, hour and minute
    if(thisWeek and nextAlarm == currentTime[3:6]):
        print('current alarm' + str(nextAlarm))
        return 0
    else:
        print('next alarm' + str(nextAlarm))
        return calcDiffDates(currentTime[3:6],nextAlarm)
 
    
    

def ntpSetTime():
    try:
        from ntptime import settime
        settime()
    except OSError as e:
        print('Error while ntp syncing: '+str(e))

def manualStart():
    t=checkTimeToAlarm()
        
    if(t>0):
        setSleep(t)
        triggerSleep()

def init():
    print('reset clause: ' + str(machine.reset_cause()))
    
    # check if the device woke from a deep sleep
    if machine.reset_cause() == machine.DEEPSLEEP_RESET:
        print('woke from a deep sleep')
        
        t=checkTimeToAlarm()
        
        if(t<=0): #alarm NOW, trigger action
            return True
        elif(t>0): #alarm date not yet reached
            print('new sleep round')
            setSleep(t)
            triggerSleep()
    else:
        print('woke normal')
    
    return False
        
