import time
import psutil

print("CPU: \t Mem: \t Swap: \t CPU Temp:\n")

while(1):
	print(psutil.cpu_percent(),"\t",psutil.virtual_memory().percent,"\t",psutil.swap_memory().percent,"\t",psutil.sensors_temperatures()["cpu_thermal"][0][1])
	time.sleep(1)
