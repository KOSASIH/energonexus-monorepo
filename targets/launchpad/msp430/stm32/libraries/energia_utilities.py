import time

def delay(milliseconds):
    time.sleep(milliseconds / 1000.0)

def millis():
    return int(time.time() * 1000)

def micros():
    return int(time.time() * 1000000)
