from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice  
import time
device = MonkeyRunner.waitForConnection()  
while True:
	device.touch(570, 1330, "DOWN_AND_UP")
	time.sleep(0.05)