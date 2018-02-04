import time

def GetTime(fmt):
    t1 = time.time()
    loc = time.localtime(t1)
    return time.strftime(fmt, loc)

if __name__ == '__main__':
   print(GetTime('%Y-%m-%d %H:%M:%S')) 
