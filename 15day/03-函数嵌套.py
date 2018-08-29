import time
def sw():
    for i in range(10):
        print('上网')
        time.sleep(0.5)
    fight()
def yxt():
    for i in range(10):
        print('拳皇')
        time.sleep(0.5)
    fight()
def fight():
    for i in range(5):
        print('男女双打')
sw()
yxt()
