from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice  
import time
time.sleep(0.1)
device = MonkeyRunner.waitForConnection()  
device.touch(10, 10, "DOWN_AND_UP")
time.sleep(0.225)
device.touch(10, 10, "DOWN_AND_UP")
time.sleep(0.6)
device.touch(10, 10, "DOWN_AND_UP")
time.sleep(1.6)
device.touch(10, 10, "DOWN_AND_UP")
time.sleep(0.9)
device.touch(10, 10, "DOWN_AND_UP")

time.sleep(2.1)
device.touch(10, 10, "DOWN_AND_UP")
time.sleep(0.4)
device.touch(10, 10, "DOWN_AND_UP")
time.sleep(0.65)
device.touch(10, 10, "DOWN_AND_UP")
time.sleep(0.5)
device.touch(10, 10, "DOWN_AND_UP")

time.sleep(3.1)
device.touch(10, 10, "DOWN_AND_UP")
time.sleep(0.4)
device.touch(10, 10, "DOWN_AND_UP")





