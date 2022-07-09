
time = int(input('Enter the time in seconds: '))
hours = time // 3600
minutes = (time - hours * 3600) // 60
seconds = time - (hours * 3600 + minutes * 60)
print(f"time {hours} : {minutes} : {seconds}")







