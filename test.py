# -*- coding: utf-8 -*-
import uiautomator
import adb
import time 
import threading
ACCOUNT_PASS = {"12345678@163.com":"qqqqqqqq",
        "1234@163.com":"qqqqqqqq",
        "12345@163.com":"qqqqqqqq",
        "123456@163.com":"qqqqqqqq",
        "1234567@163.com":"qqqqqqqq",
        "22222222@163.com":"qqqqqqqq",
        "33333333@163.com":"qqqqqqqq",
        "44444444@163.com":"qqqqqqqq"
        }


class watchThread(threading.Thread):
    def __init__(self,arg):
        super(watchThread,self).__init__()
        self.arg =arg
        print "arg:",arg
    def setWatcher(self):
        if self.arg and self.arg.exists():
            self.arg.watcher("back").when(text = "帐号或密码错误，请重新输入").press.back()
    def run(self):
        if self.arg and self.arg.exists():
            while True:
                self.arg.watchers.run()
                time.sleep(0.5)

class LOGIN(object):
    def __init__(self):
        self.device = None
        pass
    def getDevice(self):
        if adb.checkadbtoolexists():
            self.device = uiautomator.Device()
            watchthread = watchThread(self.device)
            watchthread.setWatcher()
            watchthread.start()
    def loginWithLib(self,lib):
        if len(lib) and self.device.exists():
            
            self.device.press.home()
            textacct = u"163/QQ/Gmail/企业邮箱等"
            textpass = u"密码"
            self.device(text = u"网易邮箱大师").click()
            for account,passwd in ACCOUNT_PASS.items():
                
                self.device(index = 1,checkable ="true").click(1000,550)
                self.device(text=textacct ).set_text(account)
                self.device(text = textpass ).set_text(passwd)

                self.device(text = u"登录").click()
                time.sleep(5)
               # self.device.press.back()
                print account,passwd
                textacct = account
                textpass =passwd
            print "operate over!!" 



if __name__ == "__main__":
    login = LOGIN()
    login.getDevice()
    login.loginWithLib(ACCOUNT_PASS)
