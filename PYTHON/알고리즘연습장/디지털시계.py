hours = [i for i in range(24)]
minutes = [i for i in range(60)]
seconds = [i for i in range(60)]
cnt = 0
for hour in hours:
    for minute in minutes:
        for second in seconds:
            if hour % 10 == 3 or minute % 10 == 3  or minute - minute % 10 == 30 or second % 10 == 3 or second - second % 10 == 30 :
                cnt += 1
print(cnt)