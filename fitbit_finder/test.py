import fitbit
import datetime

def addSecs(timeval, secs_to_add):
    dummy_date = datetime.date(1, 1, 1)
    full_datetime = datetime.datetime.combine(dummy_date, timeval)
    added_datetime = full_datetime + datetime.timedelta(seconds=secs_to_add)
    return added_datetime.time()

# You'll have to gather the tokens on your own, or use
# ./gather_keys_oauth2.py
fb = fitbit.Fitbit('228MCC', '6cbffd2583f9d4aa26a25a7d58c5369d',
                             access_token='eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiI2MkJMNVAiLCJhdWQiOiIyMjhNQ0MiLCJpc3MiOiJGaXRiaXQiLCJ0eXAiOiJhY2Nlc3NfdG9rZW4iLCJzY29wZXMiOiJ3aHIgd251dCB3cHJvIHdzbGUgd3dlaSB3c29jIHdhY3Qgd3NldCB3bG9jIiwiZXhwIjoxNTA3MDI4MTc4LCJpYXQiOjE1MDY5OTkzNzh9.W4rjZa32yavp2dDQ5dswtAGd4t-NonIDJQce6v2j5Zw', refresh_token='908914028d4e395bf3a5adce96d563f9163cfebc0f15fe1543aede26b11312a9')
# atime = datetime.datetime.now().datetime()
actualtime = datetime.datetime(2017, 10, 3, 14, 5, 00, 00000)
fb.add_alarm('481851626', actualtime, ['TUESDAY'], recurring=False, enabled=True, label='Find Device Alarm', snooze_length=None, snooze_count=None, vibe='DEFAULT')
print(fb.get_devices())
