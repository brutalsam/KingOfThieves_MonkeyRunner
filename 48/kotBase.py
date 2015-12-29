from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice  
import time
time.sleep(1)
device = MonkeyRunner.waitForConnection()  
device.touch(10, 10, "DOWN_AND_UP")
time.sleep(0.086)
device.touch(10, 10, "DOWN_AND_UP")
time.sleep(1.9)
device.touch(10, 10, "DOWN_AND_UP")
time.sleep(0.29)
device.touch(10, 10, "down_and_up")
time.sleep(1.2)
device.touch(10, 10, "DOWN_AND_UP")
time.sleep(0.94)
device.touch(10, 10, "down_and_up")
time.sleep(0.717)
device.touch(10, 10, "down_and_up")


