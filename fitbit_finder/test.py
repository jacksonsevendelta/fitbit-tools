import fitbit
import datetime

def addSecs(timeval, secs_to_add):
    dummy_date = datetime.date(1, 1, 1)
    full_datetime = datetime.datetime.combine(dummy_date, timeval)
    added_datetime = full_datetime + datetime.timedelta(seconds=secs_to_add)
    return added_datetime.time()

# You'll have to gather the tokens on your own, or use
# ./gather_keys_oauth2.py
fb = fitbit.Fitbit('<client_id>', '<client_secret>',
                             access_token='<access_token>', refresh_token='<refresh_token>')
# atime = datetime.datetime.now().datetime()
actualtime = datetime.datetime(2017, 10, 3, 14, 5, 00, 00000)
fb.add_alarm('481851626', actualtime, ['TUESDAY'], recurring=False, enabled=True, label='Find Device Alarm', snooze_length=None, snooze_count=None, vibe='DEFAULT')
print(fb.get_devices())
