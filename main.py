#from Event import Event
from random import seed
from random import randint
seed(1)

# time in s; speed in bps; size in B
bucket_size = 200
bucket = bucket_size
p_size = 0
rate = 20000
exceed = 0
conform = 0

endTime = 0.05
currentTime = 0
oldTime = 0
time_interval = 0
p_num = 10
packets = []
i = 1
#t_on = 10
#t_off = 5

if p_size != 0:
	packets = [p_size] * p_num
else:
	while i <= p_num:
		packets.append(randint(5, 200))
		i += 1
	print(packets)

i = 1
while currentTime < endTime:
    currentTime += 0.01 #krok jaki sobie wybierzemy
    print ("ct = ", currentTime)
    time_interval = currentTime - oldTime
    print ("ti = ", '%.2f'%time_interval)
    bucket = min( (bucket + time_interval * rate / 8), bucket_size)
    print ("bucket = ", bucket)
    print ("L = ", p_size)
    """if bucket >= p_size:
        bucket -= p_size
        conform += 1
        print("pakiet zgodny")"""
    if bucket >= packets[i]:
        bucket -= packets[i]
        conform += 1
        print("pakiet zgodny")
    else:
        exceed += exceed
        print("pakiet odrzucony")
    oldTime = currentTime
    i += 1
	

if __name__ == '__main__':
    print ("conform = ", conform)
    print ("exceed = ", exceed)
