from datetime import datetime, timedelta
# 
# time = "115040.000".split('.')
# time = time[0]
# print(time)
# date = "260624"
# date_time = time+date
# print(date_time)
# print(len(date_time))
# datetime_format = "%H%M%S%d%m%y" 
# if len(date_time) ==12:
#     datetime_O = datetime.strptime(date_time,datetime_format)
#     print(datetime_O)
#     print(type(datetime_O))
# else:
#     pass

def date_formating(date_time):
    if len(date_time) ==12:
        datetime_format = "%H%M%S%d%m%y" 
        utc_time = datetime.strptime(date_time, datetime_format)
        ist_diff = timedelta(hours=5, minutes=30)
        ist_time = utc_time+ist_diff
        # print(ist_time)
        return ist_time
    
    else:
        datetime_format = "%H%M%S" 
        utc_time = datetime.strptime(date_time,datetime_format)
        ist_diff = timedelta(hours=5, minutes=30)
        ist_time = utc_time+ist_diff
        time = str(ist_time).split(' ')
        time = time[1]
        # print(time)
        # print(type(ist_time))
        # print(ist_time)
        return time
# date_formating("115040")



