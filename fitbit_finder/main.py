import fitbit
import datetime

def addSecs(timeval, secs_to_add): # credit: https://stackoverflow.com/a/100776
    dummy_date = datetime.date(1, 1, 1)
    full_datetime = datetime.datetime.combine(dummy_date, timeval)
    added_datetime = full_datetime + datetime.timedelta(seconds=secs_to_add)
    return added_datetime.time()

# You'll have to gather the tokens on your own, or use
# ./gather_keys_oauth2.py
fb = fitbit.Fitbit('<client_id>', '<client_secret>',
                             access_token='<access_token>', refresh_token='<refresh_token>')

# The following is to get the alarm time. Default set to 20 seconds past now.
# Yes, my variable names are horrible.
asecpass = datetime.datetime.now().time()
a = datetime.datetime.now().time()
datenow = datetime.datetime.now().date()
datetimenow = datetime.datetime.now()
addeda = addSecs(a, 20) # change this to change no. of secs past now
alarm_time = datetime.datetime.combine(datenow, addeda)
reccurance = ['MONDAY','TUESDAY','WEDNESDAY','THURSDAY','FRIDAY','SATURDAY','SUNDAY'] # All days are here, don't change this

# CHANGE YOUR DEVICE ID HERE (TO FIND OUT YOUR DEVICE ID RUN get_devices())
device_id = '481851626'

# Sets alarm
fb.add_alarm(device_id, alarm_time, reccurance, recurring=False, enabled=True, label='Find Device Alarm', snooze_length=None, snooze_count=None, vibe='DEFAULT')

# Informs user
print("\n")
print("The datetime now is "+str(datetimenow))
print("An alarm will go off on your FitBit at approx. "+str(alarm_time))
