import os
import sys

DEBUG = 1

def printlog(log):
    funcName = sys._getframe().f_back.f_code.co_name 
    print "["+funcName+"]:"+log 

def printdebug(log):
    if DEBUG:
        print log


def checkadbtoolexists():
    ret = os.popen("whereis adb")
    ret = ret.read()
    ret1 = ret.split(":")[1]
    printlog(ret1)
    if ret1 != "\n":
        printlog("adb exsit!")
        return 1  
    else:
        print "adb is not exists!"
        return 0 
#@return :  
def check_device_exist():
    if checkadbtoolexists():
        ret =os.popen("adb devices")
        devicelist = ret.readlines()
        if len(devicelist) <= 1:
            print "device is not exists!!!"
            return None
        else:
            dlist = []
            for index in xrange(len(devicelist)):
                if index != 0 and devicelist[index] != "\n":
                    dlist.append(devicelist[index].split('\tdevice')[0])
            printdebug(dlist)
    else:
        pass



if __name__ == "__main__":
    check_device_exist()
