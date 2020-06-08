#from Event import Event

# time in s; speed in bps; size in B
bucket_size = 200
bucket = bucket_size
p_size = 100
rate = 20000
exceed = 0
conform = 0

#startTime = 0
endTime = 0.05
currentTime = 0
oldTime = 0
time_interval = 0
#events = []

while currentTime < endTime:
    currentTime += 0.01 #krok jaki sobie wybierzemy
    print ("ct = ", currentTime)
    time_interval = currentTime - oldTime
    print ("ti = ", '%.2f'%time_interval)
    bucket = min( (bucket + time_interval * rate / 8), bucket_size)
    print ("bucket = ", bucket)
    print ("L = ", p_size)
    if bucket >= p_size:
        bucket -= p_size
        conform += 1
        print("pakiet zgodny")
    else:
        exceed += exceed
        print("pakiet odrzucony")
    oldTime = currentTime
	

if __name__ == '__main__':
    print ("conform = ", conform)
    print ("exceed = ", exceed)
