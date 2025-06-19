import datetime

current_time = datetime.datetime.now()
current_ts =  current_time.timestamp() 

print(f"Seconds since January 1, 1970: {current_ts:,.4f} or {current_ts:.2e} in scientific notation")
print(f"{current_time:%b %d %Y}")