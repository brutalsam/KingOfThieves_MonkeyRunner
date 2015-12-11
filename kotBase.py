from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice  
import time
device = MonkeyRunner.waitForConnection()  
device.touch(10, 10, "DOWN_AND_UP")
time.sleep(0.15)
device.touch(10, 10, "DOWN_AND_UP")
time.sleep(0.950)
device.touch(10, 10, "DOWN_AND_UP")
