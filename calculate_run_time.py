
import time

start_time = time.time()

# program goes here
#time.sleep(67)

end_time = time.time()

total_time = end_time - start_time

# for testing
#total_time = 10000

if total_time >= 3600:
    hours = int((total_time / 60) / 60)
    minutes = int((total_time - (hours * 60 * 60)) / 60)
    seconds = int(total_time - ((minutes * 60) + (hours * 60 * 60)))
elif total_time >= 60:
    hours = 0
    minutes = int(total_time / 60)
    seconds = int(total_time - (minutes * 60))
else:
    hours = 0
    minutes = 0
    seconds = total_time

if hours == 1:
    hour_str = str(hours).strip() + " hour, "
else:
    hour_str = str(hours).strip() + " hours, "
if minutes == 1:
    minute_str = str(minutes).strip() + " minute, "
else:
    minute_str = str(minutes).strip() + " minutes, and "
if seconds == 1:
    second_str = str(seconds).strip() + " second."
else:
    second_str = str(seconds).strip() + " seconds."

run_time_str = "Program run time: %s%s%s" % (hour_str, minute_str, second_str)

print(run_time_str)
