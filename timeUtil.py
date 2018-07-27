import datetime,time

def getCurrentTime():
	return datetime.datetime.now()

def calculateTimeDiff(timeStamp_start, timeStamp_stop):
	interval = timeStamp_stop -  timeStamp_start
	return interval

def getCurrentTimeFormatted():
	ticks = time.localtime(time.time())
	return time.asctime(ticks)
