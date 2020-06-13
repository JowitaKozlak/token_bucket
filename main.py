#from Event import Event
from random import seed
from random import randint
seed(1)

# time in s; speed in bps; size in B
bucket_size = 600
bucket = bucket_size
p_size = 0
rate = 24000
exceed = 0
conform = 0

endTime = 0.6
currentTime = 0
oldTime = 0
time_interval = 0
p_num = 22
packets = []
i = 0
pr = 48000
t_on = 0.2
t_off = 0.2
#t_on = bucket_size*8/(pr-rate)
#t_off = bucket_size*8/rate
counter = 0

if p_size != 0:
    packets = [p_size] * p_num
    print(packets)
else:
    while i < p_num:
        packets.append(randint(5, 200))
        i += 1
    print(packets)

#'%.2f'%
j = 0
step = 0.02
while currentTime <= endTime:
    if counter == t_on + 0.02:
        currentTime = round(currentTime + t_off - 0.02,2)
        counter = 0
    else:
        #step = round(packets[j]*8/pr,2)
        print ("ct = ", currentTime)
        time_interval = round(currentTime - oldTime,2)
        print ("ti = ", time_interval)
        bucket = round(min((bucket + time_interval * rate / 8), bucket_size))
        print ("bucket = ", bucket)
        print ("L = ", packets[j])
        if bucket >= packets[j]:
            bucket -= packets[j]
            conform += 1
            print("pakiet zgodny")
        else:
            exceed += 1
            print("pakiet odrzucony")
        j += 1
        oldTime = currentTime
        counter = round(counter + step,2)
        currentTime = round(currentTime + step,2) #krok jaki sobie wybierzemy
	

if __name__ == '__main__':
    print ("conform = ", conform)
    print ("exceed = ", exceed)
