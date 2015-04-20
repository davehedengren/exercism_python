import datetime
import calendar

class MeetupDayException(Exception):
    pass

def meetup_day(year,month,day,suf):
    # convert day to number
    days_of_week = 'Monday Tuesday Wednesday Thursday Friday Saturday Sunday'
    day_num = days_of_week.split().index(day)
    # find the date of first day in month
    last_day = datetime.date(year,month,calendar.monthrange(year,month)[1])
    month_first = datetime.date(year,month,1)
    month_first_wd = month_first.weekday()
    
    # if counting iterations of weekday
    if suf[0] in ['1','2','3','4','5']:
        nth = int(suf[0])
        # how many weeks until nth week
        if day_num < month_first_wd:
            day_move = 7-(month_first_wd-day_num)
        elif day_num >= month_first_wd:
            day_move = day_num-month_first_wd
        first_day = month_first + datetime.timedelta(days=day_move)
        # count forward in weeks until nth
        mu_date = first_day + datetime.timedelta(days=(nth-1)*7)
        if mu_date.month != month:
            raise MeetupDayException
        else:
            return mu_date

    # if last day
    elif suf[0] == 'l':
        # cycle to find the date of the last Day (M, T, W, etc.)
        last_day_wd = last_day.weekday()
        while day_num != last_day_wd:
            last_day = last_day - datetime.timedelta(days=1)
            last_day_wd = last_day.weekday()
        return last_day

    # if teenth
    elif suf[0] == 't':
        for x in range(13,19):
            date_day = datetime.date(year,month,x).weekday()
            if date_day == day_num:
                return datetime.date(year,month,x) 

