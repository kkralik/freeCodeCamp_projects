def add_time(start, duration, day = None):
    start_list = start.split(' ')
    days, hours, minutes = 0, 0, 0
    ### UNIFYING TIME INTO [days, hours, minutes]
    hours = int(start.split(':')[0]) + int(duration.split(':')[0])
    minutes = int(start.split(':')[1].split()[0]) + int(duration.split(':')[1].split()[0])
    if start.split()[1] == 'PM':
        hours += 12
    elif start.split(':')[0] == '12':
        hours -= 12
    
    ### RECOUNTING INTO 24H SCHEME + EXTRA DAYS
    while minutes > 59:
        hours += 1
        minutes -= 60
    days = 0
    while hours > 23:
        days += 1
        hours -= 24
    pm = False
    if hours > 11:
        hours -= 12
        pm = True
    hours_options = [12, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    result = str(hours_options[hours]) + ':' + '{0:0>2}'.format(minutes)
    if pm == True:
        result += (' PM')
    else:
        result += (' AM')
    ### ADDING WEEKDAY, IF SPECIFIED
    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    if day != None:
        for d in range(7):
            if weekdays[d].lower() == day.lower():
                temp = days + d
                if int(temp%7) > len(weekdays)-1:
                    while int(temp%7) > len(weekdays)-1:
                        temp -= 7
                weekday = weekdays[int(temp%7)]
                result += ', '+ weekday

    
    ### ADDING NUMBER OF PASSED DAYS
    if days == 1:
        result += ' (next day)'
    elif days > 1:
        result += ' ({number} days later)'.format(number = days)

    return result
