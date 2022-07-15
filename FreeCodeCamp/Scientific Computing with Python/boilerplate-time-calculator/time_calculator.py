def add_time(start, duration, day='null'):
  days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
  startData = start.split(':')
  startHour = int(startData[0])
  minuteAndEnding = startData[1].split(' ')
  startMinute = int(minuteAndEnding[0])
  startEnding = minuteAndEnding[1]

  if(startHour=='12'):
    if(startEnding == 'AM'):
      startHour=0
  elif(startEnding == 'PM'):
      startHour+=12

  durationSplit = duration.split(':')
  durationHour = int(durationSplit[0])
  durationMinute = int(durationSplit[1])

  finalMinute = startMinute + durationMinute

  if(finalMinute>59):
    startHour+=1
    finalMinute-=60

  finalHour = startHour + durationHour

  daysAhead = int(finalHour/24)

  finalHour = finalHour%24

  if(finalHour>11):
    if(finalHour != 12):
      finalHour-=12
    finalEnding='PM'
  else:
    if(finalHour==0):
      finalHour=12
    finalEnding='AM'

  finalMinuteStr=str(finalMinute)
  if(finalMinute<10):
    finalMinuteStr='0'+str(finalMinute)

  new_time=str(finalHour)+':'+finalMinuteStr+' '+finalEnding

  if(day!='null'):
    day=day.capitalize()
    dayNumber=0
    for i in range(0,6):
      if(day==days[i]):
        dayNumber=i
        break
    finalDay=dayNumber+daysAhead
    finalDay=finalDay%7
    new_time+=', '+days[finalDay]

  if(daysAhead == 1):
    new_time+=' (next day)'
  elif(daysAhead>1):
    new_time+=' ('+str(daysAhead)+' days later)'


  return new_time